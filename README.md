# Kantactz
This is a Django Project for Managing the contacts or addressbook for the users.

# Features
1. Users can signup themselves. 
2. Password reset functionality provided, so if for any reason, user has locked out himself, he can use this functionality to get un-block himself.
3. User can view only his contacts. If accessed others details, 403 page will be shown.
4. Added RestFul APIs to the project which supports CRUD operation, so contacts can be created using APIs from other frontends as well. Currently BasicAuthentication being Implemented.
5. Only authenticated and authorized users can work with APIs. 

# Developer Specific 
1. Error Pages will be shown for respective errors, like, 404, 500, 403 errors.
2. SQL queries are being spit out in the Django server logs (they are not being stored in a log file as of now)
3. Reset emails will be stored in a File System. For production, a valid SMTP should be used as well as settings to be updated as well.
4. If you are using POSTMAN or Curl, make sure to pass the Authentication information as well before sending any request.

# Setup the project locally
## Clone this repository
```
$ mkdir <your-project-directory>
$ cd <your-project-directory>
$ git clone git@github.com:TechStuffBoy/Kantactz.git .
```
## Install Python
Django is a python framework, so it is mandatory to install it first. I used python 3.9.*.
Download here, https://www.python.org/downloads/
## Create virtual environment and acivate it
```
$ python -m venv venv
$ source venv/bin/activate (Mac/Linux)
$ .\venv\Scripts\activate (Windows)
$ pip install --upgrade pip (Updates pip to latest revision)
```
The above procedure will create the virtual environment for the project.
## Install the dependencies to venv
```
Make sure you are in the project directory.
$ pip install -r requirements.txt
```
## Start the django server
All secrets should be provided in a .env file. like, SECRET_KEy, DEBUG , DB Related values. A .env.sample file has been provided, please make use of it.
```
$ cp .env.sample .env
Make sure to give different SECRET_KEY and Make DEBUG=False, so that custom error pages will be shown as per the status code.
```
## Database settings
I am using the Sqlite Database here. If this project is deployed to AWS or Heroku, then we might have to use the Postgres or any similar database. You have to install pysopg2-binary (Postgres) from https://pypi.org/project/psycopg2-binary/

In kantactz/settings.py, Change, 
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
``` 
to,
```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config('DB_NAME'),
        "USER": config('DB_USER'),
        "PASSWORD": config('DB_PASSWORD'),
        "HOST": config('DB_HOST'),
        "PORT": config('DB_PORT', default=5432, cast=int)
    }
}
Note: All the above values(DB_NAME, DB_USER, etc..) should be present in .env file.
```
## Migrate the database
```
$ python manage.py makemigrations (Not needed, as already it is done)
$ python manage.py migrate

Note: For Postgresql, make sure you created the database firt, then do the migration.
```

## Create superuser
```
$ python manage.py createsuperuser

And, follow the prompt.
```

## Start the server
```
$ python manage.py runserver
```

## Navigate to
```
http://127.0.0.1:8000/addressbook/

You will be re-directed to login page. Create an account for yourself and login with that account.
```

## Note
```
1. Make sure to set DEBUG=False in .env file to see any error pages.
2. Collectstatic command, to serve all the static assets (when DEBUG=False)
$ python manage.py collectstatic
```


## Screenshots of web-app
### List Page
![ListPage](https://user-images.githubusercontent.com/17155643/179344013-f29c2b9e-2a34-4e6b-be79-e647577cee11.png)

### Edit Form
![Edit Form](https://user-images.githubusercontent.com/17155643/179344179-fab1e44e-fc2f-47f1-8276-d6801f25e0ef.png)

### Login, Sign-Up and Reset Password
![Login_Signup_Reset_Pawword](https://user-images.githubusercontent.com/17155643/179344300-1e66db92-1784-4cfd-bb25-cba2c62232e1.png)


## RestFul API
```
1. API has been created only for Contacts or Addressbook.
2. Before accessing, username and password should be given (Only Basic Authentication being used)
```

### Endpoints

#### List all the contacts [GET]
```
$ curl --user "your_username":"password" -iX GET localhost:8000/api/v1/contacts/
```

#### List only one contact [GET]
```
$ curl --user "your_username":"password" -iX GET localhost:8000/api/v1/contacts/25/
```

#### PATCH a particular field for a contact [PATCH]
```
$ curl --user "your_username":"password" -iX PATCH -H "Content-Type: application/json" -d '{ "name": "API 1" }' localhost:8000/api/v1/contacts/39/
```

#### Create a contact [POST]
```
$ curl --user "your_username":"password"-iX POST -H "Content-Type: application/json" -d '{ "name": "Api_1", "number": "9878786789", "country_code": "91", "email": "api1@example.com", "email2": "api1@business.com" }' localhost:8000/api/v1/contacts/
```
#### Delete a contact [DELETE]
```
$ curl --user "your_username":"password" -iX DELETE localhost:8000/api/v1/contacts/43/
```






