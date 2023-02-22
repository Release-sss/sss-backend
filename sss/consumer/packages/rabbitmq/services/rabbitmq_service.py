from urllib.parse import quote

from django.conf import settings

from .asynchronous_consumer import ExampleConsumer, ReconnectingExampleConsumer

amqp_url = f"amqp://{settings.RABBITMQ_USER}:{quote(settings.RABBITMQ_PASSWORD)}@{settings.RABBITMQ_HOST}/{settings.RABBITMQ_VIRTUAL_HOST}"
consumer = ReconnectingExampleConsumer(amqp_url)
consumer.run()
