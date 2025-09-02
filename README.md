# MedRotate - Backend API

**The backend API for the MedRotate application, built with Python and Flask. It's designed to handle data persistence and user management for the frontend.**

Deployment Status: [https://yourappname.railway.app](https://yourappname.railway.app) (*Replace with your Railway URL*)

## 👨‍💻 A Beginner's Backend Journey

Hello world! This is my first foray into backend development. As someone who started with frontend, building an API that serves data felt like unlocking a new superpower. This document walks through my process of building a RESTful API from scratch, the challenges I faced, and how I got it deployed live on the internet.

## 🚀 Overview

This is a RESTful API that provides endpoints for the MedRotate frontend to perform CRUD (Create, Read, Update, Delete) operations on two main resources:
*   **Rotations:** Clinical rotations like "Cardiology" or "Pediatrics".
*   **Notes:** The individual notes taken by a student during a rotation.

The backend is currently deployed on **Railway.app**.

## 🛠️ Tech Stack

I chose a simple but powerful stack to learn the fundamentals:

*   **Python 3:** The core programming language, known for its readability.
*   **Flask:** A lightweight and beginner-friendly web framework. It gave me just what I needed without overwhelming complexity.
*   **Flask-CORS:** An extension to handle Cross-Origin Resource Sharing, which is essential for letting my frontend talk to my backend on a different domain.
*   **Railway:** For deployment. Its integration with GitHub made continuous deployment smooth.

## 📡 API Endpoints (Current)

| Method | Endpoint | Description | Status |
| :--- | :--- | :--- | :--- |
| `GET` | `/api/health` | A simple health check to see if the API is running. | ✅ Implemented |
| `GET` | `/api/test` | A test endpoint to confirm the frontend-backend connection works. | ✅ Implemented |
| `GET` | `/api/rotations` | (Planned) Fetches all rotations for a user. | 🚧 *Not Started* |
| `POST` | `/api/rotations` | (Planned) Creates a new rotation. | 🚧 *Not Started* |
| `GET` | `/api/notes` | (Planned) Fetches all notes for a specific rotation. | 🚧 *Not Started* |
| `POST` | `/api/notes` | (Planned) Creates a new note. | 🚧 *Not Started* |

*The core data endpoints are not yet implemented as the database connection is the next step.*

## 🧪 Development Process & Learning Journey

1.  **Local Setup:** I started by creating a virtual environment (`venv`) to manage my Python packages. This was a new and important concept for me.
2.  **"Hello, World!" with Flask:** I followed the Flask quickstart guide to get a basic app running on `localhost:5000`. Seeing that "Hello, World!" in my browser was step one.
3.  **Understanding Routing:** I learned how the `@app.route` decorator works to map URLs to Python functions.
4.  **Returning JSON:** I discovered the `jsonify` function to send JSON responses back to the frontend instead of HTML.
5.  **The CORS Hurdle:** This was a massive "Aha!" moment. My frontend requests were blocked until I learned about CORS and installed `Flask-CORS`. Adding `CORS(app)` fixed it instantly.
6.  **Deployment Struggle:** I initially tried to deploy on Heroku. I created a `Procfile` and a `requirements.txt` file, but I ran into some compatibility issues. I didn't give up! I pivoted to **Railway**, which had a simpler workflow by connecting directly to my GitHub repo. Seeing the deployment logs pass successfully on Railway was a huge win.

## ⚠️ Challenges Faced

*   **Understanding How APIs Work:** The concept of the frontend requesting data from a separate server was abstract at first. Using the browser's Network tab to see the requests and responses made it click.
*   **Environment Variables:** Learning how to use `os.environ` to hide sensitive data (like secret keys and later, database URLs) was crucial for deployment.
*   **Deployment Errors:** My first deployments failed due to missing packages in `requirements.txt`. I learned to carefully check the build logs—they are your best friend when something goes wrong.
*   **The Mental Shift:** Switching from frontend logic (DOM manipulation) to backend logic (request handling, data processing) was the biggest challenge and the most valuable learning experience.

## 🔮 Next Steps & Future Improvements

The next chapter for this backend is the most exciting one:

*   **Integrate a Database:** The immediate next step is to connect a **PostgreSQL** database using an ORM like SQLAlchemy or a driver like `psycopg2`.
*   **Implement Auth:** Add user registration and login using JWT (JSON Web Tokens) to secure the API endpoints.
*   **Build Out Endpoints:** Fully implement the planned CRUD endpoints for rotations and notes.
*   **Data Validation:** Add validation to ensure only clean data gets into the database.
*   **Error Handling:** Implement robust error handling to return helpful error messages to the frontend.

*This backend is the foundation. It's not much to look at yet, but it's live and it's mine. I'm incredibly proud of getting this far and can't wait to bring it to life with a database. The journey continues!*
