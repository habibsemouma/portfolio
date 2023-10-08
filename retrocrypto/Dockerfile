FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt ./
COPY . ./

RUN pip install -r requirements.txt



CMD ["gunicorn", "-w","4","-b","0.0.0.0:80","wsgi:app"]
