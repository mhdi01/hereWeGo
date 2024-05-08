# New Challenge Django Project

This Django project serves as a RESTful API backend for a new challenge.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python (>=3.6)
- PostgreSQL
- pip package manager

## Installation

1. **Clone the repository to your local machine:**

   ```bash
   git clone https://github.com/mhdi01/hereWeGo.git
   
2. **Navigate to the project directory:**
   ```bash
   cd newChallenge
   
3. **Install project dependencies:**
   ```bash
   pip install -r requirements.txt

4. **Install PostgreSQL:**
   
   *on linux*
   ```bash
     sudo apt-get update
     sudo apt-get install postgresql postgresql-contrib
   ```
   *on macOS*
   ```bash
   brew install postgresql
6. **Create a PostgreSQL database for the project:**
   ```bash
   CREATE DATABASE herewego;
7. **Apply database migrations:**
```bash
python manage.py makemigrations
python manage.py migrate
```

## Usage

**Running the Development Server**
To start the Django development server, run:

```bash
python manage.py runserver
```
By default, the server will run at http://127.0.0.1:8000/.

**Accessing the Admin Interface**
To access the Django admin interface, create a superuser:

```bash
python manage.py createsuperuser
```
Then, navigate to http://127.0.0.1:8000/admin/ in your web browser and log in with the superuser credentials.

**API Endpoints**
The API endpoints are accessible at http://127.0.0.1:8000/api/.


## Configuration

# Settings
The project settings are located in newChallenge/settings.py. You can configure database settings, authentication, and other options in this file.

# Database
The project is configured to use PostgreSQL as the default database. Update the DATABASES setting in settings.py with your PostgreSQL credentials.
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'herewego',
        'USER': 'yourusername',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
Replace 'yourusername' and 'yourpassword' with your PostgreSQL username and password, respectively.

# Authentication
The project uses JWT authentication provided by the rest_framework_simplejwt package. Users can obtain JWT tokens by authenticating with their credentials.

# Running Tests
python manage.py test



   
