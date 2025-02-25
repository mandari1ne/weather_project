### Weather Query Web Application

This project is developed using Django and PostgreSQL.
PyCharm is used as the development environment.

## Installation and Setup
**1. Clone the repository:**
```bash
   git clone https://github.com/mandari1ne/weather_project.git
   cd weather_project
```

**2. Set up PostgreSQL:**
You need to download and install pgAdmin4 for PostgreSQL.

  Create a new user with:
  - Username: admin
  - Password: admin
  - Change privileges and grant all permissions to the user.

  Create a new database named weather and set admin as the owner

**3. Install dependencies:**
Open PyCharm, navigate to the directory containing requirements.txt:
```bash
  cd weather_project
  pip install -r requirements.txt
```
**4. Apply database migrations:**
```bash
   python manage.py makemigrations
   python manage.py migrate
```
## Running the Application
***Option 1:*** Run with Docker
```bash
docker run --name postgres_db -e POSTGRES_DB=weather -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=admin -p 5432:5432 -d postgres:13

docker build -t django_app .

docker run --name django_app --link postgres_db:postgres_db -p 8000:8000 -d django_app
```
link: http://127.0.0.1:8000/

When you start the application for the very first time, use these commands in the terminal. This will create the containers. After that, you can start them using Docker Desktop. First, start the database container, and then start the application container.

***Option 2:*** Run without Docker
If you run the project without Docker, you need to change the database settings in settings.py.

Find this block:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'weather',
        'USER': 'admin',
        'PASSWORD': 'admin',
        'HOST': 'postgres_db',
        'PORT': '5432'
    }
}
```
Replace it with:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'weather',
        'USER': 'admin',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
```
Then, run the application:
```bash
python manage.py runserver
```
link: http://127.0.0.1:8000/

## If everything is set up correctly, the application will start.
***You will see:***
  - A city input field
  - A (currently empty) search history block
Enter a city name in the input field and click the button to get the current weather for that city.
