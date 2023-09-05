
FROM python:3.10-slim-buster


WORKDIR /app

COPY requirements.txt ./
COPY . ./

RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 3000


CMD ["gunicorn", "-w","4","-b","0.0.0.0:3000","wsgi:app"]
