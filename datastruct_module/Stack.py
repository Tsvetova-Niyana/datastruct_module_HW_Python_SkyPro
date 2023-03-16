from datastruct_module.Node import Node


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
