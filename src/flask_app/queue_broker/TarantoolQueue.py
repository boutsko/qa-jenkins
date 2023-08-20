from abc import ABC, abstractmethod

from AbstractMethods import IQueue
from tarantool_queue import Queue


class TarantoolQueue(IQueue):
    def __init__(self, queue_name="test", host='localhost', port=3301):
        self.queue = Queue(host, port, 0)
        self.queue_name = queue_name

    def create_queue(self):
        self.tube = self.queue.tube(self.queue_name)

    def send_message(self, message):
        self.tube.put(self.queue_name + '.put', [message])

    def consume_messages(self):
        while True:
            response = self.tube.take().data
            if response.data:
                print(f" [x] Received message: {response.data}")
            else:
                print(" [*] No messages in queue. Waiting for messages...")
                # self.queue.call('fiber.sleep', [1])

    def close_connection(self):
        self.queue.close()
