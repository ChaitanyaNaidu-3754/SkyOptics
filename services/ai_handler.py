"""
CosmosAI Handler - Advanced Multi-Provider System
Strategy:
1. Try all Gemini keys (1-5)
2. Try all OpenAI keys (1-5)
3. Fallback to Local Data
"""
import os
import base64
import google.generativeai as genai
from openai import OpenAI
from dotenv import load_dotenv
from services.astronomy_data import (
    get_chat_response as get_local_chat,
    get_dark_sky_locations,
    get_events,
    get_seasonal_constellation_info,
)
from PIL import Image
import io

load_dotenv()


class CosmosAIHandler:
    """Handles advanced key rotation across multiple providers."""
    
    def __init__(self):
        # Load up to 10 keys per provider
        self.gemini_keys = self._load_keys("GEMINI_AI_KEY")
        self.openai_keys = self._load_keys("OPEN_AI_KEY")
        
        self.current_gemini_index = 0
        self.current_openai_index = 0
        
        self.gemini_model = None
        self.openai_client = None
        
        self.gemini_exhausted = False
        self.openai_exhausted = False
        
        # Initialize providers
        if self.gemini_keys:
            self._init_gemini()
        if self.openai_keys:
            self._init_openai()
            
        print(f"[INIT] Loaded {len(self.gemini_keys)} Gemini keys and {len(self.openai_keys)} OpenAI keys")
    
    def _load_keys(self, base_name):
        """Load keys (BASE, BASE_2, ..., BASE_10)."""
        keys = []
        
        # Key 1 (no suffix)
        if os.getenv(base_name):
            keys.append(os.getenv(base_name))
            
        # Keys 2-10
        for i in range(2, 11):
            key = os.getenv(f"{base_name}_{i}")
            if key:
                keys.append(key)
        
        return keys
    
    def _init_gemini(self):
        """Initialize Gemini with current key."""
        if self.current_gemini_index < len(self.gemini_keys):
            key = self.gemini_keys[self.current_gemini_index]
            genai.configure(api_key=key)
            self.gemini_model = genai.GenerativeModel('gemini-2.0-flash-exp')
    
    def _init_openai(self):
        """Initialize OpenAI with current key."""
        if self.current_openai_index < len(self.openai_keys):
            key = self.openai_keys[self.current_openai_index]
            self.openai_client = OpenAI(api_key=key)
    
    def _rotate_gemini_key(self):
        """Rotate to next Gemini key."""
        self.current_gemini_index += 1
        if self.current_gemini_index < len(self.gemini_keys):
            print(f"[ROTATE] Switching to Gemini Key #{self.current_gemini_index + 1}")
            self._init_gemini()
            return True
        self.gemini_exhausted = True
        print("[EXHAUSTED] All Gemini keys used. Switching to OpenAI.")
        return False
    
    def _rotate_openai_key(self):
        """Rotate to next OpenAI key."""
        self.current_openai_index += 1
        if self.current_openai_index < len(self.openai_keys):
            print(f"[ROTATE] Switching to OpenAI Key #{self.current_openai_index + 1}")
            self._init_openai()
            return True
        self.openai_exhausted = True
        print("[EXHAUSTED] All OpenAI keys used. Switching to Local Mode.")
        return False
    
    def _call_gemini(self, prompt, image_bytes=None):
        """Try Gemini with automatic rotation."""
        if not self.gemini_model or self.gemini_exhausted:
            return {"success": False, "fallback": True}
        
        try:
            if image_bytes:
                image_part = {"mime_type": "image/jpeg", "data": image_bytes}
                response = self.gemini_model.generate_content(
                    [prompt, image_part],
                    generation_config=genai.types.GenerationConfig(
                        max_output_tokens=1024,
                        temperature=0.7
                    )
                )
            else:
                response = self.gemini_model.generate_content(
                    prompt,
                    generation_config=genai.types.GenerationConfig(
                        max_output_tokens=1024,
                        temperature=0.7
                    )
                )
            return {"content": response.text, "success": True, "provider": "Gemini"}
        
        except Exception as e:
            error_str = str(e).lower()
            if "429" in str(e) or "quota" in error_str or "resource" in error_str:
                if self._rotate_gemini_key():
                    return self._call_gemini(prompt, image_bytes)
            return {"success": False, "fallback": True, "error": str(e)[:100]}
    
    def _call_openai(self, prompt, image_b64=None):
        """Try OpenAI with automatic rotation."""
        if not self.openai_client or self.openai_exhausted:
            return {"success": False, "fallback": True}
        
        try:
            if image_b64:
                messages = [
                    {
                        "role": "user", 
                        "content": [
                            {"type": "text", "text": prompt},
                            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_b64}", "detail": "low"}}
                        ]
                    }
                ]
                response = self.openai_client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=messages,
                    max_tokens=1024
                )
            else:
                response = self.openai_client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=1024
                )
            
            return {
                "content": response.choices[0].message.content, 
                "success": True, 
                "provider": "OpenAI"
            }
        
        except Exception as e:
            error_str = str(e).lower()
            if "429" in str(e) or "quota" in error_str or "rate" in error_str:
                if self._rotate_openai_key():
                    return self._call_openai(prompt, image_b64)
            return {"success": False, "fallback": True, "error": str(e)[:100]}
    
    def _call_ai(self, prompt, image_b64=None):
        """Execute chain: Gemini (Keys 1-5) -> OpenAI (Keys 1-5)."""
        image_bytes = base64.b64decode(image_b64) if image_b64 else None
        
        # 1. Try Gemini Chain
        result = self._call_gemini(prompt, image_bytes)
        if result.get("success"):
            return result
            
        # 2. Try OpenAI Chain
        result = self._call_openai(prompt, image_b64)
        if result.get("success"):
            return result
            
        # 3. Fallback
        return {"success": False, "fallback": True}

    def analyze_image(self, image_b64):
        """Analyze image with full rotation support."""
        prompt = """Analyze this astronomy/sky image. Provide:

## 🔭 Sky Analysis

### Detected Objects
- List visible celestial objects (stars, planets, constellations, nebulae)

### Pattern Recognition
- **Patterns Found:** (constellation shapes, star trails, etc.)
- **Mythology:** (cultural significance)
- **Scientific Context:** (astronomical meaning)

### Viewing Info
- **Best Time:** When to observe these objects
- **Next Appearance:** When visible again
- **Tips:** Observation recommendations

Be specific and educational."""

        result = self._call_ai(prompt, image_b64)
        if result.get("success"):
            return {"content": result["content"], "provider": result.get("provider")}
        
        return self._local_image_analysis(image_b64)
    
    def _local_image_analysis(self, image_b64):
        """Local fallback analysis."""
        try:
            image_bytes = base64.b64decode(image_b64)
            img = Image.open(io.BytesIO(image_bytes)).convert('RGB')
            pixels = list(img.getdata())
            num_pixels = len(pixels)
            
            total_bright = sum((r+g+b)/3 for r,g,b in pixels)
            avg = total_bright / num_pixels
            bright_spots = sum(1 for r,g,b in pixels if (r+g+b)/3 > 200)
            
            lines = ["## 🔭 Sky Analysis (Local Mode)\n\n"]
            if avg < 50: lines.append("### Sky Quality: ★★★★★ Excellent\n")
            elif avg < 100: lines.append("### Sky Quality: ★★★★☆ Good\n")
            else: lines.append("### Sky Quality: ★★★☆☆ Fair\n")
            
            if bright_spots > num_pixels * 0.01:
                lines.append(f"\n### Detected: {bright_spots} bright points\n")
                
            seasonal = get_seasonal_constellation_info()
            lines.append(f"\n### Current Season: {seasonal['highlight']}\n")
            lines.append(f"- **Constellations:** {', '.join(seasonal['constellations'])}\n")
            
            return {"content": "".join(lines), "provider": "Local"}
        except:
            return {"error": "Image analysis failed"}

    def get_chatbot_response(self, message, history=None):
        """Chat with full rotation support."""
        prompt = f"""You are CosmosAI. Be accurate, educational, and engaging.
        
        User: {message}
        
        Guidelines:
        - Use bold for key terms
        - 2-4 paragraphs
        - Include interesting facts
        """
        
        result = self._call_ai(prompt)
        if result.get("success"):
            return f"*[{result['provider']}]* {result['content']}"
            
        local = get_local_chat(message)
        return f"*[Local Mode]* {local}"

    def suggest_dark_sky(self, city):
        """Dark sky finder with full rotation support."""
        if not city: return {"suggestion": "Please enter a city."}
        
        prompt = f"""Find stargazing spots near {city}. 
        Format:
        #### [Name] ★★★★★
        - **Distance:**
        - **Bortle:**
        - **Tips:**
        """
        
        result = self._call_ai(prompt)
        if result.get("success"):
            return {"suggestion": f"*[{result['provider']}]*\n\n{result['content']}"}
            
        local = get_dark_sky_locations(city)
        lines = [f"*[Local Mode]*\n\n## 🌃 Near {city}\n\n"]
        for loc in local['locations']:
            stars = "★" * (6 - loc['bortle']) if loc['bortle'] <= 5 else "★"
            lines.append(f"#### {loc['name']} {stars}\n- Distance: {loc['distance']}\n- Bortle: {loc['bortle']}\n\n")
        
        return {"suggestion": "".join(lines)}

    def get_fresh_events(self):
        return get_events(6)
