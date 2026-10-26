# Pandharpur Django Project

A Django web application using the `pandharpur` settings module. Consult the application views and templates for supported pages and features.

## Technology

Python, Django

## Local setup

Clone this repository, open a terminal in its root directory, and create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment, then install dependencies:

```bash
pip install django
```

For the Django project, review its settings for required environment variables and database configuration. Apply migrations and launch the local development server:

```bash
python manage.py migrate
python manage.py runserver
```

> These setup instructions reflect files checked in the repository. Successful installation and all application features have not been independently verified. Do not use development settings in production.

## Repository

[View source code](https://github.com/mipashyayalmar/pandharpur)

## Notes

Please inspect the application code and configuration before deployment. Do not commit credentials, user information, or database backups.
