# Carbon Kinn Sin x Code Mal Website Backend

This project is the backend for the Carbon Kinn Sin x Code Mal campaign website, built with Django. The backend includes user registration, JWT authentication, and a custom admin dashboard for user management.

## Features

- **User Registration**: Allows users to sign up with their name, email, phone number, and secure hashed passwords.
- **JWT Authentication**: Provides token-based authentication for secure API access.
- **Custom User Model**: Email as a unique identifier, validations for password strength, and phone format (+959).
- **Admin Dashboard**: Django’s admin interface is customized for managing user data easily.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <project-directory>


2. **Install Requirements**:
  pip install -r requirements.txt

4. **Make Migrations**:
   python manage.py makemigrations

5. **Run Migrations**:
  python manage.py migrate

6. **Create Superuser**:
  python manage.py createsuperuser

7. **Start Server**:
  python manage.py runserver
