from app import create_app
from app.extensions import db
from app.models import User

app = create_app()

with app.app_context():
    # Create all database tables
    db.create_all()
    
    # Insert predefined users
    admin = User(username="admin", password="admin123", role="admin")
    user = User(username="user", password="user123", role="user")
    
    # Add users to the database session
    db.session.add(admin)
    db.session.add(user)
    
    # Commit changes
    db.session.commit()

    print("Users inserted successfully!")
