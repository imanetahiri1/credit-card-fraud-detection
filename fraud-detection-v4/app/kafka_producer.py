import json

from confluent_kafka import Producer


KAFKA_CONFIG = {
    "bootstrap.servers": "localhost:9092",
}


def publish_transaction(
    producer: Producer,
    transaction: dict,
) -> None:
    producer.produce(
        topic="transactions",
        key=str(transaction["transaction_id"]),
        value=json.dumps(transaction),
    )
    producer.flush()