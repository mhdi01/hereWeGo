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
5. **Create a PostgreSQL database for the project:**
   ```bash
   CREATE DATABASE herewego;
6. **Apply database migrations:**
```bash
python manage.py makemigrations
python manage.py migrate


   
