# Simple App

A Flask web application with user authentication and dashboard functionality.

## Features
- User registration and login
- Dashboard with user profile management
- PostgreSQL database integration

## Prerequisites
- Docker and Docker Compose installed (for local development)

## Local Development with Docker

1. Clone the repository
2. Navigate to the project directory
3. Run the application using Docker Compose:

```bash
docker-compose up --build
```

This will start both the Flask application and PostgreSQL database.

The application will be available at http://localhost:5000

## Stopping the Application

To stop the application, press Ctrl+C in the terminal where docker-compose is running, or run:

```bash
docker-compose down
```

## Manual Installation (without Docker)

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables (see .env.example)

4. Initialize the database:
```bash
python init_db.py
```

5. Run the application:
```bash
python run.py
```

The application will be available at http://localhost:5000

## Deployment to Render

1. Fork this repository to your GitHub account
2. Sign up/login to Render (https://render.com)
3. Click "New +" and select "Web Service"
4. Connect your GitHub repository
5. Configure the service:
   - Name: flask-app (or any name you prefer)
   - Region: (select your preferred region)
   - Branch: main (or your default branch)
   - Root Directory: (leave empty)
   - Environment: Python
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python run.py`
6. Add environment variables:
   - SECRET_KEY: (set a strong secret key)
   - FLASK_ENV: production
7. Click "Create Web Service"
8. Render will automatically provision a PostgreSQL database and deploy your application

The application will be available at the URL provided by Render.