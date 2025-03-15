from flask import Flask, render_template, request, session
import json
import random
import secrets
secret_key = secrets.token_hex(16)

app = Flask(__name__)
app.secret_key = secret_key


def load_destinations():
    with open("Database/destinations.json", "r") as file:
        return json.load(file)

@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
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

if __name__ == '__main__':
    app.run(debug=True)
