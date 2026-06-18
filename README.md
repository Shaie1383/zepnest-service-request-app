# ZepNest Service Request Application

A full-stack web application developed for the **ZepNest Software Developer Internship Assignment**. The application allows users to register, log in, create service requests, upload reference images, track request status, and manage their service requests through a secure and user-friendly dashboard.

---

# Project Overview

The ZepNest Service Request Application simulates a home-service request management platform where users can raise service requests for different household services such as:

* Plumbing
* Electrical Work
* Cleaning
* Appliance Repair
* Painting
* Carpentry
* Other Home Services

Users can create and manage requests while tracking their progress through an organized dashboard.

---

# Key Features

## User Authentication

* User Registration
* User Login
* User Logout
* Password Hashing using Werkzeug
* Session Management using Flask-Login
* Protected Routes
* Secure Authentication Workflow

## Service Request Management

* Create New Service Requests
* View Request Details
* Edit Existing Requests
* Update Request Status
* Delete Requests
* Ownership-Based Access Control

## Image Upload Support

* Upload Reference Images
* JPG, JPEG, PNG Support
* Secure File Validation
* Request Image Preview

## Dashboard Features

* Request Statistics
* Search Requests
* Sort Requests
* Status Tracking
* Responsive Dashboard Interface

## Security Features

* Password Hashing
* Session-Based Authentication
* Protected Routes
* Ownership Validation
* File Upload Restrictions
* CSRF Protection
* Server-Side Validation

## Error Handling

* Custom 403 Error Page
* Custom 404 Error Page
* Custom 500 Error Page
* Form Validation Feedback
* Graceful Exception Handling

---

# Technology Stack

## Frontend

* HTML5
* CSS3
* Bootstrap 5
* JavaScript

## Backend

* Python 3
* Flask

## Database

* MySQL

## ORM

* Flask-SQLAlchemy

## Authentication

* Flask-Login

## Forms and Validation

* Flask-WTF
* WTForms

## Additional Libraries

* Werkzeug
* Pillow
* PyMySQL
* python-dotenv
* Gunicorn

---

# System Workflow

User Registration
↓
User Login
↓
Dashboard
↓
Create Service Request
↓
Store Request in MySQL Database
↓
View / Edit / Delete Request
↓
Track Request Status

---

# Database Design

## Users Table

| Column        | Description           |
| ------------- | --------------------- |
| id            | Primary Key           |
| name          | User Name             |
| email         | User Email            |
| password_hash | Encrypted Password    |
| created_at    | Account Creation Time |

### Relationship

One User → Many Service Requests

---

## Service Requests Table

| Column         | Description         |
| -------------- | ------------------- |
| id             | Primary Key         |
| user_id        | Foreign Key         |
| title          | Request Title       |
| description    | Request Description |
| category       | Service Category    |
| address        | Service Address     |
| preferred_date | Preferred Date      |
| preferred_time | Preferred Time      |
| status         | Request Status      |
| image_path     | Uploaded Image      |
| created_at     | Creation Time       |
| updated_at     | Last Update Time    |

---

# Project Structure

```text
zepnest-service-request-app/
│
├── app.py
├── config.py
├── requirements.txt
├── Procfile
├── schema.sql
├── README.md
├── .env.example
├── .gitignore
│
├── forms/
│   ├── login_form.py
│   ├── registration_form.py
│   └── request_form.py
│
├── models/
│   ├── user.py
│   └── service_request.py
│
├── routes/
│   ├── auth.py
│   └── requests.py
│
├── templates/
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── create_request.html
│   ├── edit_request.html
│   ├── request_details.html
│   ├── 403.html
│   ├── 404.html
│   └── 500.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── uploads/
│
├── screenshots/
│
└── postman/
    └── zepnest_collection.json
```

---

# Installation Guide

## Step 1: Clone Repository

```bash
git clone <repository-url>
cd zepnest-service-request-app
```

## Step 2: Create Virtual Environment

```bash
python -m venv venv
```

## Step 3: Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

## Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 5: Configure Environment Variables

Create a `.env` file in the project root.

```env
SECRET_KEY=your_secret_key

MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=zepnest_db
```

---

# Database Setup

Create a MySQL database:

```sql
CREATE DATABASE zepnest_db;
```

Alternatively, execute the provided:

```text
schema.sql
```

file using MySQL Workbench.

---

# Running the Application

```bash
python app.py
```

Application URL:

```text
http://127.0.0.1:5000
```

---

# Postman Collection

Import:

```text
postman/zepnest_collection.json
```

into Postman.

Available API tests:

* User Registration
* User Login
* Create Request
* View Request
* Edit Request
* Delete Request

---

# Screenshots

The project includes screenshots for:

* Home Page
* Registration Page
* Login Page
* Dashboard
* Create Request Form
* Request Details Page
* Edit Request Page
* Status Update Workflow

---

# Testing Performed

The application was tested for:

* User Registration
* User Login
* User Logout
* Session Handling
* Protected Routes
* Request Creation
* Request Editing
* Request Deletion
* Image Upload
* Request Status Updates
* Dashboard Search
* Dashboard Statistics
* Error Handling

---

# Future Enhancements

* Admin Dashboard
* Service Provider Module
* Request Assignment System
* Email Notifications
* SMS Notifications
* Cloud Storage Integration
* REST API Expansion
* Role-Based Access Control
* Payment Integration

---

# Assignment Deliverables

* Source Code
* GitHub Repository
* README Documentation
* Database Schema
* Postman Collection
* Project Screenshots
* Demo Video

---

# Author

**Shaista Mulla**

Developed as part of the **ZepNest Software Developer Internship Evaluation Project**.

---

# License

This project is intended for educational and internship evaluation purposes.
