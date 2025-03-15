from flask import Flask, render_template, request, session, redirect, url_for
import json
import random
import secrets
import bcrypt
from flask_sqlalchemy import SQLAlchemy
from functools import wraps

# Initialize Flask app
app = Flask(__name__)
app.secret_key = secrets.token_hex(32)  # Generate a random secret key

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Custom Decorator for Authentication
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'email' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Database Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, email, password, name):
        self.name = name
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

# Create Database Tables
with app.app_context():
    db.create_all()

# Helper Functions
def load_destinations():
    with open("Dataset/destinations.json", "r") as file:
        return json.load(file)

# Routes
@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    destinations = load_destinations()
    destination = random.choice(destinations)
    
    session['current_destination'] = destination
    
    return render_template(
        "quiz.html",
        clues=destination["clues"],
        options=destination["options"],
        city=destination["city"],
        country=destination["country"]
    )

@app.route("/check_answer", methods=["POST"])
@login_required
def check_answer():
    user_answer = request.form.get("option")
    destination = session.get('current_destination', {})
    
    result = {
        "is_correct": user_answer == destination.get("city", ""),
        "user_answer": user_answer,
        "correct_answer": f"{destination.get('city', '')}, {destination.get('country', '')}",
        "fun_facts": random.sample(destination.get("fun_fact", []), 2),
        "trivia": random.sample(destination.get("trivia", []), 1)
    }

    return render_template("result.html", result=result)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        if not all([name, email, password]):
            return render_template('register.html', error='All fields are required')

        if User.query.filter_by(email=email).first():
            return render_template('login.html', error='Email already registered')

        try:
            new_user = User(name=name, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            return render_template('register.html', error=str(e))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = session.pop('login_error', None)

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not all([email, password]):
            session['login_error'] = 'All fields are required'
            return redirect(url_for('login'))

        user = User.query.filter_by(email=email).first()
        
        if not user:
            session['login_error'] = 'User does not exist'
            return redirect(url_for('register'))
        
        if not user.check_password(password):
            session['login_error'] = 'Invalid credentials'
            return redirect(url_for('login'))
        
        session['email'] = user.email
        return redirect(url_for('dashboard'))

    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)  
