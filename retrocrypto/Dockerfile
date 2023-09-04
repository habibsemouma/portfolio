
FROM python:3.10-slim-buster


WORKDIR /app

COPY requirements.txt ./
COPY . ./

RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 4000


CMD ["python", "main.py"]
