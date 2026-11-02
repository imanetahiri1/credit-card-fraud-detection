import json
from datetime import datetime, timezone
from pathlib import Path

from confluent_kafka import Consumer, Producer

from app.kafka_producer import KAFKA_CONFIG
from app.model_service import FraudModelService


PREDICTIONS_PATH = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "predictions.jsonl"
)

CONSUMER_CONFIG = {
    **KAFKA_CONFIG,
    "group.id": "fraud-prediction-service",
    "auto.offset.reset": "earliest",
}


def main() -> None:
    model_service = FraudModelService()
    consumer = Consumer(CONSUMER_CONFIG)
    producer = Producer(KAFKA_CONFIG)

    PREDICTIONS_PATH.parent.mkdir(parents=True, exist_ok=True)
    consumer.subscribe(["transactions"])

    print("Prediction consumer is running...")

    try:
        while True:
            message = consumer.poll(1.0)

            if message is None:
                continue

            if message.error():
                print(f"Kafka error: {message.error()}")
                continue

            transaction = json.loads(message.value().decode("utf-8"))
            result = model_service.predict(transaction)

            prediction = {
                "transaction_id": transaction["transaction_id"],
                **result,
                "processed_at": datetime.now(timezone.utc).isoformat(),
                "model_version": "xgboost_tuned",
            }

            producer.produce(
                topic="fraud_predictions",
                key=transaction["transaction_id"],
                value=json.dumps(prediction),
            )
            producer.flush()

            with PREDICTIONS_PATH.open("a", encoding="utf-8") as file:
                file.write(json.dumps(prediction) + "\n")

            consumer.commit(message)
            print(f"Processed transaction: {transaction['transaction_id']}")

    except KeyboardInterrupt:
        print("Prediction consumer stopped.")

    finally:
        consumer.close()


if __name__ == "__main__":
    main()