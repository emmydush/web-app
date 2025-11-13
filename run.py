import os
from app import create_app, db
from app.models import User

# Determine the configuration based on environment
config_name = os.environ.get('FLASK_ENV', 'default')

app = create_app()

# Only create tables if they don't exist
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    # Use 0.0.0.0 to make the app accessible from outside the container
    # Port is determined by RENDER_PORT env var or defaults to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False if config_name == 'production' else True, host='0.0.0.0', port=port)