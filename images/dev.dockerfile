FROM python:3.10

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

# Sleep for 2 seconds to give the database time to start running
ENTRYPOINT sleep 2s && python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000
