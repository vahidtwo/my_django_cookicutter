cd /app/
python manage.py clearcache
python manage.py migrate
python manage.py collectstatic --no-input
