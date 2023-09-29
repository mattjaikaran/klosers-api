
# Heroku 

web: gunicorn api.asgi:application -k uvicorn.workers.UvicornWorker --lifespan on 

release: python3 manage.py migrate --no-input