from PIL import Image
import io
import base64

def compress_image(image_file, max_size=1024):
    """
    Compress image to max 1024px and return base64 string.
    image_file: FileStorage object from Flask or bytes.
    """
    try:
        img = Image.open(image_file)
        
        # Convert to RGB if RGBA (to save as JPEG)
        if img.mode == 'RGBA':
            img = img.convert('RGB')
            
        # Resize if larger than max_size
        if max(img.size) > max_size:
            img.thumbnail((max_size, max_size))
            
        # Save to buffer
        buffer = io.BytesIO()
        img.save(buffer, format="JPEG", quality=85)
        buffer.seek(0)
        
        # Encode to base64
        img_str = base64.b64encode(buffer.read()).decode('utf-8')
        return img_str
    except Exception as e:
        print(f"Error compressing image: {e}")
        return None
