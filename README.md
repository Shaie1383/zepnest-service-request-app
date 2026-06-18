# Service Request Application

Production-quality Flask web application for the ZepNest Software Developer Internship assignment. Authenticated users can register, log in, create home service requests, upload request images, and manage only their own records.

## Features

- User registration, login, and logout
- Password hashing with Werkzeug
- Session management with Flask-Login
- Service request CRUD with ownership checks
- Image upload support for JPG, JPEG, and PNG files
- Dashboard search, pagination, sorting, and request statistics
- Bootstrap 5 responsive UI with flash messages and validation feedback
- Friendly 403, 404, and 500 error pages

## Technology Stack

- Frontend: HTML5, Bootstrap 5, Vanilla JavaScript
- Backend: Python 3, Flask
- Database: MySQL
- ORM: Flask-SQLAlchemy
- Authentication: Flask-Login
- Forms: Flask-WTF, WTForms
- Security and utilities: Werkzeug, python-dotenv, Pillow

## Project Structure

```
service_request_app/
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── schema.sql
├── .env.example
├── .gitignore
├── uploads/
├── models/
├── routes/
├── forms/
├── templates/
├── static/
├── postman/
└── screenshots/
```

## Installation

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Copy `.env.example` to `.env` and set your values.

## Environment Variables

- `SECRET_KEY`
- `MYSQL_HOST`
- `MYSQL_USER`
- `MYSQL_PASSWORD`
- `MYSQL_DATABASE`

## Database Setup

1. Create a MySQL database named in `.env`.
2. Run `schema.sql` in MySQL Workbench or the MySQL CLI.
3. Update your `.env` file with the correct credentials.

## Running the Application

```bash
python app.py
```

Then open `http://127.0.0.1:5000` in your browser.

## Postman Collection Usage

Import `postman/zepnest_collection.json` into Postman.
Set the `base_url` variable to your local server URL.
Use the collection to test registration, login, request creation, request details, edit, and delete flows.

## Screenshots

Add submission screenshots to the `screenshots/` folder before final submission. Suggested captures:

- Home page
- Registration page
- Login page
- Dashboard
- Create request form
- Request details view
- Edit request form
- Error pages

## Notes

- Uploaded files are stored in `uploads/` and are not committed to git.
- Users can only access and manage their own service requests.
- Dashboard search works across title and category fields.
