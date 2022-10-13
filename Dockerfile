FROM python:3.10-buster

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# CMD ["gunicorn", "--bind", "0.0.0.0:5001", "app:app"]
EXPOSE 5001

LABEL org.opencontainers.image.source="https://github.com/richardokonicha/tg-subscription"

CMD ["python", "main.py"]
