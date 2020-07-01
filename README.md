# django-sqs-celery-template

An effortlessly pre configured Django, Celery and SQS template repository for those who want to process asynchronous background tasks.

## Getting started

### Requirements

Before running this app we will need:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Running locally (docker-compose)

Inside the cloned repository folder:

1. Copy the .env.example

```
cp .env.example .env
```


2. Build and run the app:

```
docker-compose up
```

That's it! After building and running the app your should have 5 container services available on your machine. Now you can start developing your application and your async background tasks!
