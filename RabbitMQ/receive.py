import pika

def message_received(ch, method, properties, body):
    print(f"Recieved new message :{body}")

# Establish connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a queue named
channel.queue_declare(queue='hello')

# Set up a consumer and specify the callback function
channel.basic_consume(queue='hello', on_message_callback=message_received, auto_ack=True)

print('Waiting for messages. To exit press CTRL+C')

# Start consuming messages
channel.start_consuming()
