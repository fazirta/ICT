 ![logo](https://github.com/fazirta/ICT/raw/master/docs/images/logos/logo.png)
 
 # ICT MAN 4 Jakarta

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![MySQL](https://img.shields.io/badge/mysql-%2307405e.svg?style=for-the-badge&logo=mysql&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)

This repository contains the Django application which powers [ictman4jkt.com](https://ictman4jkt.com/).

 ![screenshot](https://github.com/fazirta/ICT/raw/master/docs/images/screenshots/1.png)

## Installation

Install using pip: `pip install -r requirements.txt`

If you don't have pip, install it as follows:
- OS X / Linux computer, execute under the terminal:

     ```
     curl http://peak.telecommunity.com/dist/ez_setup.py | python
     curl https://bootstrap.pypa.io/get-pip.py | python
     ```

Windows computers:

     Download http://peak.telecommunity.com/dist/ez_setup.py and https://raw.github.com/pypa/pip/master/contrib/get-pip.py, double-click to run.

## Run

  Modify `ICT/settings.py` to modify the database configuration as follows:

```python
DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'name',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'user',
        'PASSWORD': 'password',
        'OPTIONS': {
          'autocommit': True,
        },
    }
}

```

### Create database

Execute in the terminal:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Create superuser

  Execute under the terminal:
```bash
python manage.py createsuperuser
```

### Collect static files
Execute under the terminal:
```bash
python manage.py collectstatic
```

### Start operation:
Execute: `python manage.py runserver`


Open the browser: http://127.0.0.1:8000/ to see the effect.

## Server Deployment

This project already supports the use of FTP Deploy for automated deployment.