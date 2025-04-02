from app import db, create_app
from app.models import User

app = create_app()

with app.app_context():
    # Check if the admin user already exists
    existing_admin = User.query.filter_by(username="admin").first()

    if not existing_admin:
        admin_user = User(username="admin", password="admin123", role="admin")  # Correctly set password
        db.session.add(admin_user)
        db.session.commit()
        print("Admin user created successfully!")
    else:
        print("Admin user already exists. Updating password...")

        # Ensure the password is set correctly
        existing_admin.password = User(username="temp", password="admin123").password  # Hash the new password
        db.session.commit()
        print("Admin password updated successfully!")
