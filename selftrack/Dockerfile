FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt ./
COPY . ./

RUN pip install -r requirements.txt


EXPOSE 7000


CMD ["gunicorn", "-w","4","-b","0.0.0.0:7000","wsgi:app"]
