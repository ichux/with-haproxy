import json
import signal
import sys
import urllib.parse

from confluent_kafka import Consumer, KafkaError
from sqlalchemy import URL, Column, Integer, MetaData, String, Table, create_engine

# Kafka configuration
kafka_bootstrap_servers = "localhost:9092"
kafka_topic = "example_topic"


pg_table_name = "example_table"


convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

# Define PostgreSQL table schema
# metadata = MetaData(naming_convention=convention, schema="public')
metadata = MetaData(naming_convention=convention, schema=None)
example_table = Table(
    pg_table_name,
    metadata,
    Column("id", Integer, primary_key=True),
    Column("message", String),
)


def connection_setting(password):
    return f"postgresql+psycopg2://username:{urllib.parse.quote_plus(password)}@localhost:5432/dbname"


# Create Kafka consumer
consumer = Consumer(
    {
        "bootstrap.servers": kafka_bootstrap_servers,
        "group.id": "my_consumer_group",
        "auto.offset.reset": "earliest",
    }
)

# Subscribe to Kafka topic
consumer.subscribe([kafka_topic])

# engine = create_engine(connection_setting("kx@jj5/g"))
engine = create_engine(
    URL.create(
        "postgresql+psycopg2",
        username="dbuser",
        # plain (unescaped) text
        password="kx@jj5/g",
        host="pghost10",
        database="appdb",
    )
)


# Function to consume messages from Kafka and insert into PostgreSQL
# noinspection PyTypeChecker
def consume_and_insert():
    for msg in consumer:
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # End of partition, the consumer reached the end
                continue
            else:
                print(msg.error())
                break

        # Insert message into PostgreSQL
        with engine.connect() as conn:
            conn.execute(
                example_table.insert().values(
                    message=json.loads(msg.value().decode("utf-8"))
                )
            )


# Set up signal handler for SIGINT
signal.signal(signal.SIGINT, lambda signal_, frame: (consumer.close(), sys.exit(0)))

if __name__ == "__main__":
    consume_and_insert()
