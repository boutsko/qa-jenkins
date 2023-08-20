from queue_broker.RabbitMqConnection import RabbitMQConnectionS


class SendMessageRabbitController:
    def __init__(self):
        self.rabbitmq = RabbitMQConnectionS()

    def send_message_rabbit(self, queue_name, message):
        self.rabbitmq.create_queue(queue_name)

        self.rabbitmq.send_message(queue_name, message=message)
        self.rabbitmq.close_connection(queue_name)

    def create_vm(self):
        self.send_message_rabbit(queue_name="create_vm", message="create vm")

    def stop_vm(self):
        self.send_message_rabbit(queue_name="stop_vm", message="stop vm")

    def start_vm(self):
        self.send_message_rabbit(queue_name="start_vm", message="start vm")

    def snapshot_vm(self):
        self.send_message_rabbit(queue_name="snapshot_vm", message="snapshot vm")
