
FROM python:3.10-slim-buster

RUN apt-get update && \
    apt-get install -y ffmpeg && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt ./
COPY . ./

RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 3000


CMD ["gunicorn", "-w","4","-b","0.0.0.0:3000","wsgi:app"]
