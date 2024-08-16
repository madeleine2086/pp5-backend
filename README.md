<br />

<h2>BOOK|tagram API</h2>

<h1 id="contents">Contents</h1>


-   [Introduction](#introduction)
-   [Database Schema](#database-schema)
-   [User Stories](#user-stories)
-   [Agile Methodology](#agile-methodology)
-   [Technologies Used](#technologies-used)
    -   [Languages](#languages)
    -   [Frameworks, libraries, and Programs](#frameworks-libraries-and-programs)
-   [Testing Automated and Manual](TESTING.md)
-   [Bugs](#bugs)
-   [Project Setup](#project-setup)
-   [Deployment](#deployment)
-   [Credits](#credits)
-   [Acknowledgements](#acknowledgements)

## Introduction

This repository is the backend API utilising the Django REST Framework(DRF).

The React frontend project repository can be found [// here //](https://pp5front-c44116638555.herokuapp.com/)

<br />


## Database Schema
<h2 id="#database-schema"></h2>

<img src="documentation/database-schema.png">



<h2 id="user-stories">User Stories</h2>

- As an authenticated user I can login
- As an authenticated user I can edit my profile
- As an authenticated user I can create a comment
- As an authenticated user I can edit a comment
- As an authenticated user I can delete a comment
- As an authenticated user I can create a post
- As an authenticated user I can edit a post
- As an authenticated user I can delete a post
- As an authenticated user I can like other users posts
- As an authenticated user I can follow other users
- As an authenticated user I can add a review of a product
- As an authenticated user I can update a review of a product
- As an authenticated user I can delete a review of a product
- As an authenticated user I can logout




<h2 id="agile-methodology">Agile Methodology</h2>
The Agile Methodology was used to plan this project, implemented through Github and the Project Board.
Project Board can be seen here: https://github.com/users/madeleine2086/projects/3/



## Testing
<h2 id="testing"></h2>
<h3>Manual tests have been performed on this API:</h3>
-   All CRUD functionalites for Post model, Comment model, Review model have been checked in the admin functionality of an API, all are working

<h3>Automated tests:<h3>
-   Created automated tests for comments, reviews, posts, profiles apps.
-   all passed:
<img src="documentation/backend-tests.png">



## Bugs
-   Cors Header error when signing in access not allowed
-   This was resolved by adding the following to the settings.py:
<br />
if 'CLIENT_ORIGIN' in os.environ:
<br />
    CORS_ALLOWED_ORIGINS = [
        <br />
        os.environ.get('CLIENT_ORIGIN')
        <br />
    ]
    <br />
<br />
if 'CLIENT_ORIGIN_DEV' in os.environ:
<br />
    extracted_url = re.match(
        <br />
        r'^.+-', os.environ.get('CLIENT_ORIGIN_DEV', ''), re.IGNORECASE
        <br />
    ).group(0)
    <br />
    CORS_ALLOWED_ORIGIN_REGEXES = [
        <br />
        rf"{extracted_url}(eu|us)\d+\w\.codeinstitute-ide\.net$",
        <br />
    ]
    <br />

CORS_ALLOW_CREDENTIALS = True


## Technologies Used

<a href="#top">Back to the top.</a>

### Languages

- Python - Django REST API

### Frameworks, libraries, and Programs


- Django Cloudinary Storage

- Django Filter

- PyJWT

- psycopg

- Pillow

- Git

- Github

- Gitpod

- Heroku

- Django Rest Auth

- PostgreSQL

- gunicorn

- Cors headers




## Project Setup

Use the Code Institutes full template to create a new repository, and open it in Gitpod.

Install Django by using the terminal command:

- pip3 install 'django<4'
- start the project using the terminal command:
django-admin startproject drf_api . 
- The dot at the end initializes the project in the current directory.
- Install the Cloudinary library using the terminal command:
- pip install django-cloudinary-storage
- Install the Pillow library for image processing capabilities using the terminal command:
pip install Pillow

Go to settings.py file to add the newly installed apps, the order is important:
<hr />
INSTALLED_APPS = [
    <br />
    'django.contrib.admin',
    <br />
    'django.contrib.auth',
    <br />
    'django.contrib.contenttypes',
    <br />
    'django.contrib.sessions',
    <br />
    'django.contrib.messages',
    <br />
    'cloudinary_storage', 
    <br />
    'django.contrib.staticfiles',
    <br />
    'cloudinary',
    <br />
]
<br />
<br />
Create an env.py file in the top directory
<br />
In the env.py file and add the following for the cloudinary url:
<br />
<br />
import os
<br />
os.environ["CLOUDINARY_URL"] = "cloudinary://API KEY HERE"
<br />
<br />
In the settings.py file set up cloudinary credentials, define the media url and default file storage with the following code:
<br />
<br />
import os
<br />

if os.path.exists('env.py'):
<br />
    import env
    <br />
    <br />

CLOUDINARY_STORAGE = {
    <br />
    'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
    <br />
}
<br />
MEDIA_URL = '/media/'
<br />
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
<br />
<br />
Workspace is now ready to use.



## Deployment

<a href="#top">Back to the top.</a>

- Install JSON Web Token authentication by using the terminal command:
<br />
pip install dj-rest-auth
<br />
- In settings.py add these 2 items to the installed apps list:
<br />
'rest_framework.authtoken'
<br />
'dj_rest_auth'
<br />
<br />
- In the main urls.py file add the rest auth url to the patetrn list:
<br />
path('dj-rest-auth/', include('dj_rest_auth.urls')),
<br />
<br />
- Migrate the database using the terminal command:
<br />
python manage.py migrate
<br />
<br />
- To allow users to register install Django Allauth:
<br />
pip install 'dj-rest-auth[with_social]'
<br />
<br />

- In settings.py add the following to the installed app list:
<br />
'django.contrib.sites',
<br />
'allauth',
<br />
'allauth.account',
<br />
'allauth.socialaccount',
<br />
'dj_rest_auth.registration',
<br />
<br />
- also add the line in settings.py
<br />
SITE_ID = 1
<br />
<br />
- In the main urls.py file add the registration url to patterns:
<br />
 path(
    <br />
        'dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')
        <br />
    ),
    <br />
    <br />
- Install the JSON tokens with the simple jwt library:
<br />
pip install djangorestframework-simplejwt
<br />
<br />
- In env.py set DEV to 1 to check wether in development or production
<br />
os.environ['DEV'] = '1'
<br />
<br />
- In settings.py add an if/else statement to check development or production:
<br />
REST_FRAMEWORK = {
    <br />
    'DEFAULT_AUTHENTICATION_CLASSES': [(
        <br />
        'rest_framework.authentication.SessionAuthentication'
        <br />
        if 'DEV' in os.environ
        <br />
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
        <br />
    )],
    <br />
    <br />
- Add the following code in settings.py
<br />
REST_USE_JWT = True # enables token authentication
<br />
JWT_AUTH_SECURE = True # tokens sent over HTTPS only
<br />
JWT_AUTH_COOKIE = 'my-app-auth' #access token
<br />
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token' #refresh token
<br />
<br />
- Create a serializers.py file in the foodsnap_api file(project file name)
- Copy the code from the Django documentation UserDetailsSerializer as follows:
<br />
from dj_rest_auth.serializers import UserDetailsSerializer
<br />
from rest_framework import serializers
<br />


class CurrentUserSerializer(UserDetailsSerializer):
    """Serializer for Current User"""
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta(UserDetailsSerializer.Meta):
        """Meta class to to specify fields"""
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image'
        )
- In settings.py overwrite the default User Detail serializer:
<br />
REST_AUTH_SERIALIZERS = {
    <br />
    'USER_DETAILS_SERIALIZER': 'drf_api.serializers.CurrentUserSerializer'
    <br />
}
<br />
<br />
- Run the migrations for database again

- Update the requirements file with the following terminal command
<br />
pip freeze > requirements.txt
<br />
- Make sure to save all files, add and commit followed by pushing to Github.



## Credits
- This project was made possible due to help of tutoring team and analysing lots of public repositories:
    - Code Institute "Moments" walkthrough helped me setup the base for BOOK|tagram
    - https://github.com/JaqiKal
    - https://github.com/artcuddy 
    - I'd like to thank everyone in Code institute, my family for still speaking to me, and my friend Colm for being a very good website user.


## Acknowledgements


<a href="#top">Back to the top.</a>
