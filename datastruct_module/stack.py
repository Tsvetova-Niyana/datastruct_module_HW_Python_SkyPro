from datastruct_module.node import Node


class Stack:
    def __init__(self, top=None):
        self.top = top

    def push(self, data):
        """ Добавления данных в стэк.
            Создание экземпляра Node, для связывания данных в стеке, происходит прям в методе push"""

        node_new = Node(data)
        next_top = self.top
        self.top = node_new
        self.top.next_node = next_top


    def pop(self):
        """Реализуйте метод `pop()` класса `Stack`.

            Метод удаляет из стека верхний элемент (последний добавленный), реализуя правило
            LIFO (Last In, First Out) и возвращает данные удаленного экземпляра класса `Node`."""

        if self.top == None:
            return None
        removed = self.top.data
        self.top = self.top.next_node

        return removed
