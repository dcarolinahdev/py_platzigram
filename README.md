# Platzigram app
inspired by instagram app

## Requirements and versions

- ***Django=2.1.5***

Don't forget this ubuntu dependencies:
```
sudo apt-get install python3-pip python3-dev postgresql postgresql-contrib libpq-dev git nginx
```

Pillow dependencies:
```
sudo apt-get install libjpeg-dev
```

### Initial server configuration

Let's create a new user with no home directory that has the ability to run some super user commands:
```
sudo useradd -g sudo -M <username>
```

We assign a strong password to the new user:
```
sudo passwd <username>
```

We log in with the new user:
```
su <username>
```

### Configure PostgreSQL

We first log in as the postgres user using the command `sudo su postgres` and then type `psql` to enter the PostgreSQL interactive shell where we configure the following:

1. We create a database:

```
CREATE DATABASE <db_name>;
```

2. We create a user for the database:
```
CREATE USER <db_user> WITH PASSWORD 'db_user_passw';
```

3. We give permissions to the user on the database:
```
GRANT ALL PRIVILEGES ON DATABASE <db_name> TO <db_user>;
```

Leave
```
\q
exit
```

### About Environment Variables

You can add to ~/.bashrc any (or all) of the following variables:

```
export PLATZI_SECRET_KEY="random_key:aasdafasf"
export PLATZI_DB_NAME="platzi"
export PLATZI_DB_USER="freddier"
export PLATZI_DB_PASSWORD="cvander<3"
export PLATZI_DB_PORT="5432"
export PLATZI_DB_HOST="localhost"
export DJANGO_SETTINGS_MODULE="platzi.settings.prod"
```
```
source ~/.bashrc
```
```
nano platzi/settings/prod.py

ALLOWED_HOSTS = ['myapp.io']
```

---
---

# Bibliography

- [Curso Django Platzi 2018](https://platzi.com/cursos/django-2018/)

- [My own note taking about python](https://github.com/dcarolinahdev/notes/blob/master/python.md)

- [My own note taking about django](https://github.com/dcarolinahdev/notes/blob/master/django.md)
