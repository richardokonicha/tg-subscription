docker build -t tg-subscription/main:v1 .

# docker compose --env-file .env up

docker run -e WEBHOOK_URL=https://d1a1-197-210-226-110.ngrok.io -p 5001:5001 reechee/tg-subscription:v3

 docker build . --tag ghcr.io/jonashackt/hello-world:latest
        docker run ghcr.io/jonashackt/hello-world:latest
        docker push ghcr.io/jonashackt/hello-world:latest