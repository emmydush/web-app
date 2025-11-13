#!/usr/bin/env python
"""
Database initialization script
Run this to create all database tables
"""
import os
from app import create_app, db
from app.models import User

def init_db():
    """Initialize the database"""
    app = create_app()
    
    with app.app_context():
        print("Creating database tables...")
        db.create_all()
        print("✓ Database tables created successfully!")
        print("\nDatabase URI:", app.config['SQLALCHEMY_DATABASE_URI'])
        print("\nYou can now run: python run.py")

if __name__ == '__main__':
    init_db()
