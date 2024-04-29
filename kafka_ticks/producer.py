import json

from confluent_kafka import Producer

# Kafka configuration
kafka_bootstrap_servers = "localhost:9092"
kafka_topic = "example_topic"


# Create Kafka producer
producer = Producer({"bootstrap.servers": kafka_bootstrap_servers})


# Function to produce messages to Kafka
def produce_message(message):
    producer.produce(kafka_topic, json.dumps(message))
    producer.flush()


if __name__ == "__main__":
    while True:
        produce_message({"message": input("Enter a message: ")})
