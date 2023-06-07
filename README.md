# teebeauty_backend
 Beauty website backend


Source and activate the virtual environment

    source ./venv/bin/activate

Run the server

    ./manage.py runserver

Make migrations and migrate

    ./manage.py makemigrations

    ./manage.py  migrate


## DATABASE SETUP

    sudo -u postgres psql

    CREATE DATABASE tersun_db;

    CREATE USER tersun_user WITH PASSWORD 'tersun_pass';

    ALTER ROLE tersun_user SET client_encoding TO 'utf8';
    ALTER ROLE tersun_user SET default_transaction_isolation TO 'read committed';
    ALTER ROLE tersun_user SET timezone TO 'UTC';

    GRANT ALL PRIVILEGES ON DATABASE tersun_db TO tersun_user;

    \q
