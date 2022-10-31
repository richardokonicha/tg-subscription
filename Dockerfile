FROM python:3.10-buster

WORKDIR /work

COPY . .

RUN pip install -r requirements.txt

# CMD ["gunicorn", "--bind", "0.0.0.0:5001", "app:app"]
EXPOSE 5001

LABEL org.opencontainers.image.source="https://github.com/richardokonicha/tg-subscription"

CMD ["python", "main.py"]
