import pika

# Establish connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a queue named 
channel.queue_declare(queue='hello')

message = "Hello I'm sending first msg"
message2="Second Message"
# Publish a message to the 'hello' queue
channel.basic_publish(exchange='', routing_key='hello', body=message)

print(f"sent message:{message}")

# Close the connection
connection.close()
