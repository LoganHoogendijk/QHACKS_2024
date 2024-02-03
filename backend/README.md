# Setup
- python -m venv pyenv (first time only)
- add .env file to backend/qhacks/.env
- source pyenv/Scripts/activate
- cd backend/qhacks && python manage.py makemigrations && python manage.py migrate && python manage.py runserver