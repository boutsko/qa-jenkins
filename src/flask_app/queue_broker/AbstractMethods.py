from abc import ABC, abstractmethod


class AsyncIQueue(ABC):
    @abstractmethod
    async def create_queue(self):
        return NotImplemented

    @abstractmethod
    async def send_message(self, message):
        return NotImplemented

    @abstractmethod
    async def consume_messages(self):
        return NotImplemented

    @abstractmethod
    async def close_connection(self):
        return NotImplemented


class IQueue(ABC):
    @abstractmethod
    def create_queue(self, queue_name):
        return NotImplemented

    @abstractmethod
    def send_message(self, queue_name, message):
        return NotImplemented

    @abstractmethod
    def consume_messages(self, queue_name):
        return NotImplemented

    @abstractmethod
    def close_connection(self):
        return NotImplemented
