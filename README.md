# Quiz App

A simple web application to create, take, and manage quizzes.
Built with **Flask**, **MongoDB**, and vanilla **HTML/CSS/JavaScript**.

## Features
- User signup & login (JWT authentication)
- Create and store quizzes in MongoDB
- Timed quiz with auto-submit
- View your score after submission
- Search quizzes by title or topic

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/DoEhab/quiz-app.git
   cd quiz-app

2. **Install dependencies**
    pip install -r requirements.txt

3. **Configure environment variables**
    Create a .env file (if needed) with your SECRET_KEY and MongoDB URI.

4. **Run the app**
    python3 run.py

5. **Open in browser**
    http://localhost:5000/

6. **Project Structure**

    app/
 ├── controllers/     # Controllers for business logic
 ├── routes/          # Flask route blueprints
 ├── templates/       # HTML templates
 └── static/          # CSS and JavaScript files
utils/                # Helper functions and DB config

7. **License**
 Educational use.




