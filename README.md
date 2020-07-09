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

### Testing it

For the local environment you can test receiving a message on the queue according to the following steps.

- Launch a bash terminal within the web container with: 

```
docker exec -it <docker_web_id> bash
```

- Open the django shell: 

```
python src/manage.py shell_plus
```

- Import the task and execute it:

```
from payment.tasks import capture_payment
capture_payment.delay(pk=10)
```

You should see the worker docker service logs changing and a new message on the queue named "celery" if you access the panel on: http://localhost:9325

There is also the possibility of testing it through the aws-cli. To do that you need to add a new queue to the config/elasticmq.conf file because the celery queue expects the data on a specific format.

```
queues {
   default {
     defaultVisibilityTimeout = 10 seconds
     delay = 5 seconds
     receiveMessageWait = 0 seconds
   }
}
```

And now you can test it:

```
aws --endpoint-url http://localhost:9324 sqs send-message --queue-url http://localhost:9324/queue/default --message-body "Hello, queue"
```
