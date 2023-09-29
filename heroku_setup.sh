echo ">>> heroku_setup init"
#!/bin/bash

python3 manage.py migrate --no-input
