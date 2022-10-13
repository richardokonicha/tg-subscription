FROM python:3.10-buster

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# CMD ["gunicorn", "--bind", "0.0.0.0:5001", "app:app"]
EXPOSE 5001

CMD ["python", "main.py"]
