echo "db setup"

echo "dropping current db"
dropdb kloser_db
echo "db dropped"

echo "creating new db.."
createdb --username=mattjaikaran kloser_db
echo "db created"

echo "migrating..."
python3 manage.py migrate

echo "creating superuser..."
python3 manage.py create_superuser

echo ">>db setup complete"