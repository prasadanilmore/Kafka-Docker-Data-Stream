from confluent_kafka import Consumer, KafkaError

consumer_config = {
    'bootstrap.servers': 'kafka:9092',  # Kafka broker address
    'group.id': 'my-group',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(consumer_config)
topic = 'hello-topic'

consumer.subscribe([topic])

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue

    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            print('Reached end of partition')
        else:
            print(f'Error: {msg.error().str()}')
    else:
        print(f'Received: {msg.value().decode("utf-8")}')

consumer.close()
