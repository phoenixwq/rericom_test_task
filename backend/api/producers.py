from kafka import KafkaProducer
import json
from django.conf import settings


def send(data: dict):
    producer = KafkaProducer(
        bootstrap_servers=settings.BROKER_URL,
        api_version=(0, 10, 0),
        value_serializer=lambda x: json.dumps(x).encode('utf-8')
    )
    producer.send('message_topic', data)
    producer.close()
