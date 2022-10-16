
FROM python:latest

RUN  pip install --upgrade pip

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT  tail -f /dev/null

# ENTRYPOINT  python manage.py runserver