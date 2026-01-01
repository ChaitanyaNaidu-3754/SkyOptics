import os
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from services.ai_handler import CosmosAIHandler
from services.iss_service import ISSService
from services.utils import compress_image
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "cosmos_ai_super_secret_key_2026")

# Initialize Services
ai_handler = CosmosAIHandler()
iss_service = ISSService()

# --- Page Routes ---

@app.route('/')
def home():
    # Pass hardcoded events initially, or use session cache
    events = session.get('cached_events', [
        {"date": "Jan 10, 2026", "event": "Jupiter Opposition", "desc": "Jupiter closest to Earth."},
        {"date": "Feb 28, 2026", "event": "Planet Parade", "desc": "Alignment of 6 planets."},
        {"date": "Mar 3, 2026", "event": "Blood Moon", "desc": "Total Lunar Eclipse."}
    ])
    return render_template('home.html', events=events)

@app.route('/iss')
def iss_page():
    return render_template('iss.html')

@app.route('/vision')
def vision_page():
    return render_template('vision.html')

@app.route('/chat')
def chat_page():
    return render_template('chat.html')

@app.route('/counselor')
def counselor_page():
    return render_template('counselor.html')

# --- API Routes ---

@app.route('/api/iss', methods=['GET'])
def get_iss_status():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City parameter is required"}), 400
    return jsonify(iss_service.check_visibility(city))

@app.route('/api/analyze', methods=['POST'])
def analyze_sky():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    img_b64 = compress_image(file)
    if not img_b64:
        return jsonify({"error": "Image Error"}), 500
        
    return jsonify(ai_handler.analyze_image(img_b64))

@app.route('/api/chat', methods=['POST'])
def chat_api():
    data = request.json
    user_message = data.get('message')
    if not user_message: return jsonify({"error": "Empty"}), 400
    
    history = session.get('chat_history', [])
    # Convert session history to Gemini format if possible, or just pass list
    # Handler now expects list
    response_text = ai_handler.get_chatbot_response(user_message, history)
    
    # Simple history management
    history.append({"role": "user", "parts": [user_message]})
    history.append({"role": "model", "parts": [response_text]})
    session['chat_history'] = history[-6:] # Keep strictly last 6 turns
    
    return jsonify({"response": response_text})

@app.route('/api/dark-sky', methods=['POST'])
def dark_sky_api():
    data = request.json
    city = data.get('city', '')
    result = ai_handler.suggest_dark_sky(city)
    return jsonify(result)

@app.route('/api/refresh-events', methods=['POST'])
def refresh_events():
    # Only allow refresh every few mins in real app, here we just call
    new_events = ai_handler.get_fresh_events()
    if new_events:
        session['cached_events'] = new_events
        return jsonify({"status": "updated", "events": new_events})
    return jsonify({"status": "failed"}), 500

@app.route('/reset-chat', methods=['POST'])
def reset_chat():
    session.pop('chat_history', None)
    return jsonify({"status": "cleared"})

if __name__ == '__main__':
    app.run(debug=True)
