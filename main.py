from flask import Flask, render_template, request, session, redirect, flash, url_for
import json
import random
import secrets
import bcrypt
from flask_sqlalchemy import SQLAlchemy

secret_key = secrets.token_hex(16)

app = Flask(__name__)
app.secret_key = secret_key


def load_destinations():
    with open("Database/destinations.json", "r") as file:
        return json.load(file)

# @app.route("/", methods=["GET"])
@app.route("/dashboard", methods=["GET"])
def index():
    destinations = load_destinations()
    destination = random.choice(destinations)
    
    # Store destination in session for answer verification
    session['current_destination'] = destination
    
    return render_template(
        "quiz.html",
        clues=destination["clues"],
        options=destination["options"],
        city=destination["city"],
        country=destination["country"]
    )

@app.route("/check_answer", methods=["POST"])
def check_answer():
    user_answer = request.form.get("option")
    destination = session.get('current_destination', {})
    
    # Prepare result details
    result = {
        "is_correct": user_answer == destination.get("city", ""),
        "user_answer": user_answer,
        "correct_answer": f"{destination.get('city', '')}, {destination.get('country', '')}",
        "fun_facts": random.sample(destination.get("fun_fact", []), 2),
        "trivia": random.sample(destination.get("trivia", []), 1)
    }

    return render_template("result.html", result=result)

''' user auth '''

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.secret_key = 'your_secure_secret_key_here'  # Change to a random secret key
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)  # Should be unique
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, email, password, name):
        self.name = name
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/')
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        # Validate required fields
        if not all([name, email, password]):
            return render_template('register.html', error='All fields are required')

        # Check if email already exists
        if User.query.filter_by(email=email).first():
            return render_template('login.html', error='Email already registered')

        try:
            new_user = User(name=name, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            return redirect('/login')
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
            return redirect('login')

        user = User.query.filter_by(email=email).first()
        
        if not user:
            session['login_error'] = 'Email does not exist'
            return redirect('login')
        
        if not user.check_password(password):
            session['login_error'] = 'Invalid credentials'
            return redirect('login')
        
        session['email'] = user.email
        return redirect('dashboard')

    return render_template('login.html', error=error)


# @app.route('/dashboard')
# def dashboard():
#     if 'email' not in session:
#         return redirect('/login')
    
#     user = User.query.filter_by(email=session['email']).first()
#     if not user:
#         return redirect('/logout')
    
#     return render_template('dashboard.html', user=user)

# @app.route('/logout')
# def logout():
#     session.pop('email', None)
#     return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)
