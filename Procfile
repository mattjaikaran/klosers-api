
# Heroku 

web: gunicorn api.asgi:application -k uvicorn.workers.UvicornWorker

release: python3 manage.py migrate --no-input