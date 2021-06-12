# Dockerfile
FROM python:3.9
WORKDIR /api
COPY . /api
RUN pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["./docker-entrypoint.sh"]
