## Setup database

# Database -MySql


1. Install Mysql Server
    - Ensure you have MySQL installed on your system. If not, you can download and install it from the official MySQL website.

    During installation, remember the root password or create a new user with privileges to access the database.

2. Insatll mysql client for python
    - You will need to install a Python package to allow Django to communicate with MySQL
    - command
        - pip install mysqlclient

3. Create a MYSQL database
    
4. Update settings.py in Your Django Project
    - DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',  # MySQL backend
            'NAME': 'DjangoWithReact',  # Your database name
            'USER': 'your_mysql_username',  # Your MySQL username
            'PASSWORD': 'your_mysql_password',  # Your MySQL password
            'HOST': 'localhost',  # Or the IP address of your MySQL server
            'PORT': '3306',  # Default MySQL port
        }
    }

    