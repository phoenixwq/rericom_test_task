from kafka import KafkaConsumer
import json, requests, os

TOKEN = os.getenv("TOKEN")
API_URL = os.getenv("API_URL")
ROUTE = "/api/v1/message_confirmation/"
BROKER_URL = os.getenv("BROKER_URL")


if __name__ == "__main__":
    consumer = KafkaConsumer(
        'message_topic',
        api_version=(0, 10, 0),
        bootstrap_servers=BROKER_URL
    )
    for message in consumer:
        message_data = json.loads(message.value.decode())
        success = True
        if message_data.get("text") == "АБРАКАДАБРА":
            success = False
        data = {
            "message_id": message_data.get("message_id"),
            "success": success
        }
        headers = {"Authentication": TOKEN}
        resp = requests.post(
            API_URL + ROUTE,
            data=data,
            headers=headers
        )
