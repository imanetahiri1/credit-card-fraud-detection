import time
import uuid
from pathlib import Path

import pandas as pd
from confluent_kafka import Producer

from app.kafka_producer import KAFKA_CONFIG, publish_transaction


DATA_PATH = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "raw"
    / "creditcard.csv"
)


def main() -> None:
    producer = Producer(KAFKA_CONFIG)

    df = pd.read_csv(DATA_PATH).drop(columns=["Class"])

    for _, row in df.head(10).iterrows():
        transaction = {
            "transaction_id": str(uuid.uuid4()),
            **row.to_dict(),
        }

        publish_transaction(producer, transaction)
        print(f"Published transaction: {transaction['transaction_id']}")
        time.sleep(1)


if __name__ == "__main__":
    main()