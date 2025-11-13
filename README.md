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

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up PostgreSQL:
   - Install PostgreSQL if you haven't already
   - Create a new database (e.g., `web_app_db`)
   - Note your PostgreSQL credentials

5. Configure environment variables:
   - Copy `.env.example` to `.env`
   - Update the `.env` file with your PostgreSQL credentials:
     ```
     DB_USER=postgres
     DB_PASSWORD=your_password
     DB_HOST=localhost
     DB_PORT=5432
     DB_NAME=web_app_db
     ```

6. Initialize the database:
   ```bash
   python init_db.py
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

The application now uses PostgreSQL for data storage. The database configuration is managed through environment variables in the `.env` file.

**Default PostgreSQL Connection Details:**
- **Host:** localhost
- **Port:** 5432
- **User:** postgres
- **Database:** web_app_db

You can change these by updating the `.env` file.

### Using pgAdmin

To manage your PostgreSQL database with pgAdmin:
1. Open pgAdmin (usually at `http://localhost:5050`)
2. Add a new server connection with your PostgreSQL details
3. Create a new database named `web_app_db`
4. Run `python init_db.py` to initialize tables

## Technologies Used

- **Flask**: Python web framework
- **Flask-SQLAlchemy**: ORM for database operations
- **Flask-Login**: Session management and authentication
- **PostgreSQL**: Relational database
- **psycopg2**: PostgreSQL adapter for Python
- **Bootstrap 5**: CSS framework for responsive design

## Future Enhancements

- Change password functionality
- Email verification
- Profile editing
- User activity analytics
- Password reset via email
- Two-factor authentication

## License

This project is open source and available under the MIT License.
