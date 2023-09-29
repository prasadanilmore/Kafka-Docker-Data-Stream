from confluent_kafka import Producer
import time

# Configure the producer
config = {
    'bootstrap.servers': 'kafka:9092',  # Kafka broker address
    'client.id': 'python-producer'
}

# Create a Kafka producer instance
producer = Producer(config)

# Specify the topic and message
topic = 'hello-topic'
message = 'Hello, Kafka!'

while True: 
    for i in range(10):
        # Produce the message to the topic
        producer.produce(topic, value=message)
        # Wait for any outstanding messages to be delivered and delivery reports to be received
        print(f"Produced: {message}")
        time.sleep(1)

producer.flush()
