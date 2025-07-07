# Massimo AI Dockerfile — versione produzione
FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements_ottimizzati.txt

EXPOSE 8080

CMD ["python", "main.py"]
