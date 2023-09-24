
FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt ./
COPY . ./

RUN pip install -r requirements.txt


EXPOSE 4000


CMD ["gunicorn", "-k","gevent","-c","gunicorn_config.py","wsgi:app"]
