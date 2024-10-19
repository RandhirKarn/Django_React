### Prerequisites
1. Python: Install Python 3.8 or later from python.org. This will also install pip, which is used for managing Python packages.

2. Node.js: Install Node.js from nodejs.org. This includes npm, which is the package manager for JavaScript.

3. Visual Studio Code (VSCode): Download and install VSCode from code.visualstudio.com.

### Steps -
- --------------------------------------------------------------------------------------
## Step 1: Set Up the Django Backend

1. Create a Django project
    # Open your terminal and create a new directory for your project. You can name it whatever you want (e.g., DjangoReactProj):
        - mkdir DjangoReactProj
        - cd DjangoReactProj
    # Inside your project folder, create a virtual environment to isolate your project's dependencies:
        - python -m venv myenv
            - myenv is the name of virtual environment for this project. you can name it whatever you like

    # Activate the virtual environment
        - On windows (using powershell)
            - myenv\Scripts\activate
        - On windows (using gitbash)
            - source myenv/Scripts/activate

        - Always activate your virtual environment(myenv in my case)
            - It ensures that your project uses specific versions of packages and dependencies installed within myenv.
            - If your virtual environment is using a specific python version, you need to activate it to ensure your project
              is using correct interpreter and associated libraries.
            - Basically, when you activate your virtual environment, then instead of using global python environment, you ensure that your are using the packages, depedencies within the virtual environment that you have created for the project

    # Install django using pip
        - pip install django

    # create a new django project
        - django-admin startproject backend
            - This creates a new directory called backend with the necessary Django files.

    
2. Create a django App
    # change into the backend directory
        - cd backend
    # Create a new django app called api
        - python manage.py startapp api

3. Install Django REST Framework
    # This package makes it easy to build APIs with Django
        - pip install djangorestframework

4. Update Settings.py
    # Open backend/settings.py and add rest_framework and api to your INSTALLED_APPS list
        INSTALLED_APPS = [
            ...
            'rest_framework',
            'api',
        ]

        - This tells Django to include the REST framework and your new app.


# Run Migrations:
    - python manage.py makemigrations
    - python manage.py migrate

# Start the Django Server:
    - python manage.py runserver

    - You should see output indicating the server is running at http://127.0.0.1:8000/.





## Step 2: Set Up the React Frontend
1. Create a React App
    - Open a new terminal (keeping your Django server running) and navigate back to the root of your project:
        - cd..
        - npx create-react-app frontend

2. Install axios
    - Navigate to the frontend directory
        - cd frontend

    - install axios
        - npm install axios

3. run frontend
    - npm start




=================================================================================================================================
## Routes
==========
# Root directory -> DjangoReactProj
# project -> backend
# app -> api


# urls.py file at project level(backend) servers as the main router of the entire project

# Each app in Django can have its own urls.py file, where you define the routes (URLs) specific to that app. This allows you to organize routes related to a specific feature or functionality.

    - if you have created an app which is api here, you make an entry in the project level urls.py file
    
        from django.contrib import admin
        from django.urls import path, include

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('api/', include('api.urls')),  # Include routes from the api app
        ]

# inside api

    from django.urls import path
    from .views import ItemViewSet

    urlpatterns = [
        path('items/', ItemViewSet.as_view({'get': 'list', 'post': 'create'}), name='item-list'),  # List and create items
        path('items/<int:pk>/', ItemViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='item-detail'),  # Retrieve, update, delete a specific item
    ]

now, in above case, 
    for route GET api/items/, RETURNS A LIST OF ITEMS
    for route POST api/items/, CREATES AN ITEM

================================================================================================================================

## how to connect to a database
# Connecting a Django project to a database involves configuring your database settings in the settings.py
    - ensure you have the necessary database driver installed
    - for mysql
        - pip install mysqlclient
    
# Update the projects settings.py file
    For MySQL, the configuration would look like this:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'your_database_name',
            'USER': 'your_database_user',
            'PASSWORD': 'your_password',
            'HOST': 'localhost',
            'PORT': '3306',  # Default MySQL port
        }
    }





=======================================================================================================================
## Initialize GIT in the project
---------------------------------
# Go to project directory
    - in this case DjangoReactProj is the project directory

# initialize GIT
    - git init

# Add new repository as a remote
    - git remote add origin https://github.com/RandhirKarn/Django_React.git

# Add files to git
    - git add -A

# Commit your changes
    - git commit -m 'Initial commit'

# Push your project to GITHub
    - git push -u origin master
    












