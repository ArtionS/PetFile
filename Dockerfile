
FROM python:latest

RUN  pip install --upgrade pip

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 80

# ENTRYPOINT  tail -f /dev/null

ENTRYPOINT  python manage.py runserver 0.0.0.0:80