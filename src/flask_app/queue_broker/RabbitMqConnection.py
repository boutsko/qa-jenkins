import pika

from .AbstractMethods import IQueue


class RabbitMQConnectionS(IQueue):
    def __init__(self, host='localhost', port="5672"):
        credentials = pika.PlainCredentials('guest', 'guest')
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host, port, '/', credentials)
        )
        self.channel = self.connection.channel()

    def create_queue(self, queue_name):
        self.channel.queue_declare(queue=queue_name)

    def send_message(self, queue_name, message):
        self.channel.basic_publish(exchange='', routing_key=queue_name, body=message)

        print(f" [x] Sent message={message} to queue_name={queue_name}")

    def consume_messages(self, queue_name):
        self.channel.basic_consume(queue=queue_name, auto_ack=True)

        print(
            f" [*] Waiting for messages on queue_name={queue_name}. To exit press CTRL+C"
        )

        self.channel.start_consuming()

    def close_connection(self):
        self.connection.close()


# x = RabbitMQConnectionS()
# print(" [x] Connection established")
