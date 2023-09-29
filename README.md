# Simple Kafka Message Project with Docker

This project demonstrates a simple Kafka message pipeline using Docker with Confluent Kafka. It includes a Kafka producer that sends a "Hello, Kafka!" message to a Kafka topic, and a Kafka consumer that receives and prints this message.

## Prerequisites

Before you begin, make sure you have the following installed:

- Docker: [Docker Installation Guide](https://docs.docker.com/get-docker/)
- Docker Compose: [Docker Compose Installation Guide](https://docs.docker.com/compose/install/)

## Getting Started

Follow these steps to set up and run the project:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/prasadanilmore/Kafka-Docker-Data-Stream
   cd Kafka-Docker-Data-Stream

2. **Build the Docker containers using Docker Compose:**

    ```bash
    docker-compose up --build

**Observing Output:**

After running the containers, you can observe the output from both the producer and consumer in the terminal. The producer will print "Message Produced," and the consumer will print "Message received."

To stop the containers, press Ctrl+C.

**Project Structure:**

- `docker-compose.yml`: Defines the Kafka service and its configuration.
- `producer/Dockerfile.producer`: Dockerfile for the Kafka producer.
- `producer/producer.py`: Python script for the Kafka producer.
- `consumer/Dockerfile.consumer`: Dockerfile for the Kafka consumer.
- `consumer/consumer.py`: Python script for the Kafka consumer.

**Customizing the Message:**

You can customize the message sent by the Kafka producer by editing the `producer.py` script.

**Cleanup:**

To stop and remove the Docker containers and resources, run:

    ```bash docker-compose down
