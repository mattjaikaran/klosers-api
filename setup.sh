#!/bin/bash

# this script is only for local use

echo ">>> db setup - running setup.sh"

echo "dropping current db"
dropdb kloser_db
echo "db dropped"

echo "creating new db..."
createdb --username=mattjaikaran kloser_db
echo "db created"

echo "migrating..."
python3 manage.py migrate
echo "migrate successful"

echo "creating superuser..."
python3 manage.py create_superuser
echo "created superuser"

echo ">>> db setup complete"