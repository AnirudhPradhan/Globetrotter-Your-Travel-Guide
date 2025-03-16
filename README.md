# Globetrotter - Travel Guessing Game

Welcome to **Globetrotter**, an engaging and interactive travel guessing game where players explore famous destinations worldwide! Test your knowledge, learn fun facts, and enjoy a visually appealing interface inspired by global landmarks.

## Features

### 🎮 Interactive Gameplay:
- Guess destinations based on clues and trivia.
- Explore fun facts about each location.

### 🔐 User Authentication:
- Secure login and registration using hashed passwords.
- Persistent sessions for personalized gameplay.

### 📊 Profile Management:
- Track wins and losses.
- Reset stats with a single click.

### 📱 Responsive Design:
- Beautiful interface with rounded corners and a global theme.
- Optimized for desktop and mobile devices.

### 🌍 Dynamic Content:
- Destinations loaded from a JSON dataset for variety.

## 🛠 Installation

### Prerequisites
- Python 3.8 or higher
- Flask
- SQLite

### Steps to Install

#### 1️⃣ Clone the repository:
```bash
git clone https://github.com/AnirudhPradhan/Globetrotter.git
cd Globetrotter
```

#### 2️⃣ Create a virtual environment:
```bash
python -m venv myenv
source myenv/bin/activate  # For Linux/macOS
myenv\Scripts\activate     # For Windows
```

#### 3️⃣ Install dependencies:
```bash
pip install -r requirements.txt
```

#### 4️⃣ Set up the database:
```bash
python main.py
```

#### 5️⃣ Run the application:
```bash
flask run
```

🔗 Open the application in your browser at **http://127.0.0.1:5000**.

---

## 📁 Project Structure
```
Globetrotter/
├── Dataset/
│   └── destinations.json          # JSON file with destination data.
├── images/
│   └── bg.png                     # Background image.
├── instance/
│   └── database.db                # SQLite database file (auto-generated).
├── static/
│   ├── css/
│       └── styles.css             # Custom CSS for styling.
├── templates/
│   ├── base.html                  # Base template for layouts.
│   ├── login.html                 # Login page template.
│   ├── register.html              # Registration page template.
│   ├── quiz.html                  # Quiz page template.
│   ├── result.html                # Result page template.
│   └── profile.html               # Profile page template.
├── main.py                        # Flask application file.
└── README.md                      # Project documentation file.
```

---

## 🛠 Technologies Used
- **Backend:** Flask (Python)
- **Database:** SQLite
- **Frontend:** HTML, CSS, Bootstrap

---

## 🎯 How to Play
1. **Register or log in** to access the game.
2. Navigate to the **quiz dashboard** to start guessing destinations based on clues.
3. **Check your answers** and view fun facts and trivia about each location!
4. **Track your progress** on the profile page.

---

## 🤝 Contributing
Contributions are welcome! If you'd like to improve this project, please follow these steps:

1. **Fork** the repository.
2. **Create a new branch**:
   ```bash
   git checkout -b feature-name
   ```
3. **Commit your changes**:
   ```bash
   git commit -m "Add feature-name"
   ```
4. **Push to your forked repository**:
   ```bash
   git push origin feature-name
   ```
5. **Submit a pull request**.

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 📬 Contact
For any questions or suggestions, feel free to reach out:

👤 **Author:** Anirudh Pradhan  
🔗 **GitHub:** [AnirudhPradhan](https://github.com/AnirudhPradhan)

Enjoy playing **Globetrotter**! 🌍✈️

