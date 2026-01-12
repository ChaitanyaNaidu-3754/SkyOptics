import os
from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from services.ai_handler import CosmosAIHandler
from services.iss_service import ISSService
from services.utils import compress_image
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "cosmos_ai_super_secret_key_2026")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Please log in to access this page.'
login_manager.login_message_category = 'info'

# Initialize Services
ai_handler = CosmosAIHandler()
iss_service = ISSService()

# User Model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def api_login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            return jsonify({"error": "Authentication required", "login_required": True}), 401
        return f(*args, **kwargs)
    return decorated_function

# Create database
with app.app_context():
    db.create_all()

# Forms
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=150)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

# --- Authentication Routes ---

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password', 'error')
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or not next_page.startswith('/'):
            next_page = url_for('home')
        return redirect(next_page)

    return render_template('login.html', title='Sign In', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None:
            flash('Username already exists', 'error')
            return redirect(url_for('register'))

        user = User.query.filter_by(email=form.email.data).first()
        if user is not None:
            flash('Email already registered', 'error')
            return redirect(url_for('register'))

        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        flash('Congratulations, you are now a registered user!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', title='Sign Up', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/test')
def test():
    return f"User authenticated: {current_user.is_authenticated}, User: {current_user.username if current_user.is_authenticated else 'None'}"

@app.route('/protected')
@login_required
def protected():
    return f"Hello {current_user.username}! This is a protected page."

# --- Page Routes ---

@app.route('/')
@login_required
def home():
    # Pass hardcoded events initially, or use session cache
    events = session.get('cached_events', [
        {"date": "Jan 10, 2026", "event": "Jupiter Opposition", "desc": "Jupiter closest to Earth."},
        {"date": "Feb 28, 2026", "event": "Planet Parade", "desc": "Alignment of 6 planets."},
        {"date": "Mar 3, 2026", "event": "Blood Moon", "desc": "Total Lunar Eclipse."}
    ])
    return render_template('home.html', events=events)

@app.route('/iss')
@login_required
def iss_page():
    return render_template('iss.html')

@app.route('/vision')
@login_required
def vision_page():
    return render_template('vision.html')

@app.route('/chat')
@login_required
def chat_page():
    return render_template('chat.html')

@app.route('/counselor')
@login_required
def counselor_page():
    return render_template('counselor.html')

# --- API Routes ---

@app.route('/api/iss', methods=['GET'])
@api_login_required
def get_iss_status():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City parameter is required"}), 400
    return jsonify(iss_service.check_visibility(city))

@app.route('/api/analyze', methods=['POST'])
@api_login_required
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
@api_login_required
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
@api_login_required
def dark_sky_api():
    data = request.json
    city = data.get('city', '')
    result = ai_handler.suggest_dark_sky(city)
    return jsonify(result)

@app.route('/api/refresh-events', methods=['POST'])
@api_login_required
def refresh_events():
    # Only allow refresh every few mins in real app, here we just call
    new_events = ai_handler.get_fresh_events()
    if new_events:
        session['cached_events'] = new_events
        return jsonify({"status": "updated", "events": new_events})
    return jsonify({"status": "failed"}), 500

@app.route('/reset-chat', methods=['POST'])
@api_login_required
def reset_chat():
    session.pop('chat_history', None)
    return jsonify({"status": "cleared"})

if __name__ == '__main__':
    app.run(debug=True)
