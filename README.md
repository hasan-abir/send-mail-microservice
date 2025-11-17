# Send Mail Microservice

Tells the API to send the mail to the worker. And the worker gets the job done whenever it feels like it (almost the next instance, in a queue). And so, a 100 emails sent at once won't cause the endpoint any headache whatsoever, a 100 or a 1000.

By default, this project uses Mailhog as a dummy email host, but it's easy enough to configure a real world email host instead.

## Run with Docker (recommended)

`docker compose up --build`

Add `sudo` beforehand if permission is required

## Celery (Task manager)

- [Installation](https://docs.celeryq.dev/en/v5.5.3/getting-started/introduction.html#installation)
- [Configure](https://docs.celeryq.dev/en/v5.5.3/django/first-steps-with-django.html)
