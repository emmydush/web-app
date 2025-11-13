# Flask Web App with Login, Signup, and Dashboard

A simple web application built with Flask that includes user authentication and a dashboard.

## Features

- **User Authentication**
  - Sign up with username, email, and password
  - Login with username and password
  - Logout functionality
  - Secure password hashing

- **Dashboard**
  - Personalized dashboard for authenticated users
  - User profile page displaying account information
  - Responsive design with Bootstrap

- **Security**
  - Password hashing using Werkzeug
  - Flask-Login for session management
  - Protected routes requiring authentication

## Project Structure

```
.
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── models.py            # User model
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py          # Authentication routes
│   │   └── dashboard.py     # Dashboard routes
│   ├── templates/
│   │   ├── base.html        # Base template with navigation
│   │   ├── login.html       # Login page
│   │   ├── signup.html      # Sign up page
│   │   ├── dashboard.html   # Dashboard page
│   │   └── profile.html     # User profile page
│   └── static/
│       └── css/
│           └── style.css    # Custom styles
├── instance/                # Instance folder (auto-created)
│   └── app.db              # SQLite database
├── run.py                   # Application entry point
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Installation

1. Clone the repository or extract the files

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. From the project root directory, run:
   ```bash
   python run.py
   ```

2. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

## Usage

1. **Create an Account**
   - Click on "Sign Up" in the navigation menu
   - Enter a username, email, and password
   - Passwords must match
   - Click "Sign Up" to create your account

2. **Login**
   - Click on "Login" in the navigation menu
   - Enter your username and password
   - Click "Login" to access your dashboard

3. **View Dashboard**
   - Once logged in, you'll see your personalized dashboard
   - Click on "Profile" to view your account information
   - Click "Logout" to log out

## Default Secret Key

⚠️ **Important**: The application currently uses a default secret key for development. Before deploying to production, change the `SECRET_KEY` in `app/__init__.py` to a secure random string.

## Database

The application uses SQLite for data storage. The database file (`app.db`) is automatically created in the `instance/` folder when you first run the application.

## Technologies Used

- **Flask**: Python web framework
- **Flask-SQLAlchemy**: ORM for database operations
- **Flask-Login**: Session management and authentication
- **Bootstrap 5**: CSS framework for responsive design
- **SQLite**: Lightweight database

## Future Enhancements

- Change password functionality
- Email verification
- Profile editing
- User activity analytics
- Password reset via email
- Two-factor authentication

## License

This project is open source and available under the MIT License.
