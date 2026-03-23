# Sticky Notes Project

# DAUD AMAN
# 22P-9189
# BCS-8A
# WEB TECHNOLOGIES
# ASSIGNMENT 2

## Table of Contents

1. Project Overview
2. Features
3. Requirements
4. Installation and Setup
5. Project Structure
6. How to Use
7. File Descriptions
8. Database Setup
9. User Management
10. Troubleshooting

---

## Project Overview

Sticky Notes is a Django-based web application that allows users to create, organize, and manage digital sticky notes. Users must create an account and log in to access their personal notes. The application provides a simple and user-friendly interface for taking quick notes with customizable colors.

This project is built using Django, a powerful Python web framework, and SQLite database for data storage.

---

## Features

### User Authentication
- User registration with secure password validation
- Login and logout functionality
- Each user can only access their own notes
- Password strength validation with multiple rules

### Note Management
- Create new notes with title and content
- Edit existing notes
- Delete notes with confirmation
- View all personal notes in one place
- Search notes by title or content

### Customization
- Choose custom colors for each note
- Pin important notes to keep them at the top
- Notes are sorted by pin status and last update time

### Security
- User data is protected and isolated
- CSRF protection enabled
- Secure session management
- Password validation rules enforced

---

## Requirements

### System Requirements
- Python 3.8 or higher
- pip package manager
- Any text editor or IDE

### Python Packages
The following packages are required (included in Django installation):
- Django 3.2 or higher
- Python built-in libraries (os, pathlib)

---

## Installation and Setup

### Step 1: Install Python
Ensure you have Python 3.8 or higher installed on your system.

### Step 2: Install Django
Open your terminal or command prompt and run:

```
pip install django
```

### Step 3: Navigate to Project Directory
Change to the project directory:

```
cd sticky_project
```

### Step 4: Apply Database Migrations
Run migrations to create the database and tables:

```
python manage.py migrate
```

### Step 5: Create a Superuser (Optional)
To access the admin panel:

```
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### Step 6: Run the Development Server
Start the Django development server:

```
python manage.py runserver
```

The application will be available at: http://127.0.0.1:8000/

---

## Project Structure

```
sticky_project/
├── manage.py                 # Django management script
├── db.sqlite3                # SQLite database file
├── README.md                 
│
├── sticky_project/           # Main project folder
│   ├── __init__.py
│   ├── settings.py           # Project settings and configuration
│   ├── urls.py               # Main URL routing
│   ├── wsgi.py               # Web server interface
│   └── __pycache__/
│
└── notes/                    # Notes application folder
    ├── migrations/           # Database migration files
    │   ├── __init__.py
    │   ├── 0001_initial.py   # Initial database schema
    │   └── __pycache__/
    │
    ├── templates/            # HTML template files
    │   └── notes/
    │       ├── base.html             # Base template
    │       ├── note_list.html        # List all notes
    │       ├── note_form.html        # Create/edit note form
    │       ├── note_confirm_delete.html  # Delete confirmation
    │       ├── login.html            # Login page
    │       └── register.html         # Registration page
    │
    ├── __init__.py
    ├── models.py             # Database models
    ├── views.py              # View functions (business logic)
    ├── forms.py              # Django forms for user input
    ├── urls.py               # URL patterns for notes app
    ├── admin.py              # Django admin configuration
    └── __pycache__/
```

---

## How to Use

### Creating an Account

1. Go to http://127.0.0.1:8000/
2. Click on "Register" or navigate to /register/
3. Enter a username and password
4. Click "Register" button
5. You will be automatically logged in

### Creating a Note

1. After login, you will see the notes list page
2. Click "New Note" or navigate to /notes/new/
3. Enter the note title and content
4. Choose a color from the color picker
5. Optionally check "Pin this note" to keep it at the top
6. Click "Create" to save the note

### Editing a Note

1. On the notes list, click the "Edit" button on any note
2. Modify the title, content, or color
3. Click "Save" to update the note

### Deleting a Note

1. On the notes list, click the "Delete" button on any note
2. Confirm the deletion on the confirmation page
3. Click "Delete" to permanently remove the note

### Searching Notes

1. On the notes list page, use the search box at the top
2. Type keywords to search by title or content
3. Results update automatically as you type

### Pinning Notes

1. When creating or editing a note, check the "Pin this note" checkbox
2. Pinned notes will appear at the top of the list
3. Other notes will appear below, sorted by most recent update first

---

## File Descriptions

### Settings.py

This file contains all project configuration:

- Database settings (SQLite configuration)
- Installed applications list
- Middleware for security and functionality
- Template configuration
- User authentication settings
- Password validation rules
- Static files configuration
- Login/logout redirect URLs

### Models.py

Defines the database structure for the Note model:

- title: Note heading (up to 200 characters)
- content: Main note text
- color: Hex color code (default yellow #FFFF99)
- created_at: Timestamp when note was created
- updated_at: Timestamp when note was last modified
- owner: Foreign key to User model
- pinned: Boolean to mark important notes

### Views.py

Contains all application logic functions:

- note_list: Display all notes for the logged-in user
- note_create: Create a new note
- note_edit: Modify an existing note
- note_delete: Remove a note
- register_view: Handle user registration

### Forms.py

Defines forms for user input:

- NoteForm: Form for creating and editing notes
- Fields: title, content, color, pinned status
- Widget customization for better user experience

### URLs.py

Maps URLs to views:

- Main project URLs: /admin/, /notes/, /register/, /login/, /logout/
- Notes app URLs: list, create, edit, delete

---

## Database Setup

### Automatic Setup

Database tables are created automatically when you run migrations:

```
python manage.py migrate
```

### Database Tables

The database contains:

- auth_user: User accounts and credentials
- notes_note: All notes created by users
- django_session: User session data
- Other Django system tables

### Accessing the Database

To view or manage database content directly:

1. Install a SQLite browser (DB Browser for SQLite)
2. Open the db.sqlite3 file
3. Browse tables and data visually

Or use Django admin:

1. Create a superuser: python manage.py createsuperuser
2. Go to http://127.0.0.1:8000/admin/
3. Log in with superuser credentials
4. Manage notes and users from the admin panel

---

## User Management

### User Registration

- Users must create an account with username and password
- Password must be at least 8 characters
- Password cannot be too similar to username
- Password cannot be only numbers
- Password must not be a common password

### User Authentication

- Each user is identified by their username
- Sessions are managed securely with cookies
- Users can only see their own notes
- Force login for all note operations

### User Logout

- Users can logout from the notes list page
- Logs them out and redirects to login page
- Session is cleared from the server

---



