from datastruct_module.node import Node


class Queue:
    """Создайте класс Queue, одноименной структуры данных.
        Экземпляр класса Queue инициализируется двумя атрибутами, хранящими ссылки на начало и конец очереди.
        Для пустой очереди оба эти атрибута равны None."""

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """Создайте метод enqueue для добавления данных в очередь.
        Создание экземпляра Node, для связывания данных в очереди, происходит прям в методе enqueue."""

        node_new = Node(data)

        if self.head is None:
            self.head = node_new
            self.tail = node_new
        else:
            self.tail.next_node = node_new
            self.tail = node_new

    def dequeue(self):
        """Реализуйте метод `dequeue()` класса `Queue`.
        Метод удаляет из очереди крайний левый элемент (первый добавленный),
        реализуя правило FIFO (First In, First Out) и возвращает данные удаленного экземпляра класса `Node`."""

        if self.head == None:
            return None
        else:
            removed = self.head.data
            self.head = self.head.next_node
        return removed

