# Todo Flask App

A lightweight and user-friendly Todo List web application built with Flask, leveraging SQLite for persistent data storage. This app demonstrates a modular Flask project structure using Blueprints, session-based user authentication, and dynamic task management features.

---

## 🚀 Features

- **User Authentication**: Secure login and logout with session management.
- **Task Management**: Create, view, update, and delete tasks.
- **Status Tracking**: Tasks have statuses (`Pending`, `Working`, `Done`) with easy toggling.
- **Clear All Tasks**: Quickly remove all tasks to reset your list.
- **Modular Codebase**: Utilizes Flask Blueprints to keep authentication and task logic separate.
- **Database Integration**: Uses Flask-SQLAlchemy for ORM support with SQLite.
- **Flash Messaging**: Provides instant feedback for user actions.
- **Responsive UI**: Clean and simple interface built with HTML/CSS (expandable).

---

## 🛠️ Technologies Used

- Python 3.8+
- Flask
- Flask-SQLAlchemy
- SQLite
- Jinja2 Templates
- HTML5 & CSS3

---
## 📂 Project Structure

todo-flask-app/
│
├── app/
│   ├── __init__.py          # Flask app factory and db initialization
│   ├── models.py            # SQLAlchemy models (Task)
│   ├── routes/
│   │   ├── auth.py          # Authentication routes (login/logout)
│   │   └── tasks.py         # Task management routes
│   ├── templates/           # HTML templates for UI
│   └── static/              # Static files (CSS, JS, images)
├── env/                    # Virtual environment (excluded from repo)
├── todo.db                 # SQLite database file
├── init_db.py              # Database initialization script
├── run.py                  # Main entry point to run the app
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation

---

## 💻 Getting Started

### Prerequisites

- Python 3.x installed on your system
- Git (optional, for cloning the repository)

---

### Default Credentials

| Username | Password |
| -------- | -------- |
| admin    | 1234     |

---

## ⚙️ Usage

1. Run the app with `python run.py`.
2. Login using the default credentials.
3. Add, update, and manage your tasks.
4. Clear all tasks when needed.
5. Logout securely.

---

## 📋 To-Do / Future Enhancements

- Add user registration and password hashing.
- Support multiple users with individual task lists.
- Add task due dates and priorities.
- Improve UI with frameworks like Bootstrap or Tailwind CSS.
- Add RESTful API endpoints for task management.
- Write unit and integration tests.
- Deploy to cloud platforms like Heroku or AWS.
