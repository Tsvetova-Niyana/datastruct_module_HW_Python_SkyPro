class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:
    def __init__(self):
        self.top = None


    def push(self, data):
        """ Добавления данных в стэк.
            Создание экземпляра Node, для связывания данных в стеке, происходит прям в методе push"""

        node_new = Node(data)
        next_top = self.top
        self.top = node_new
        self.top.next_node = next_top

stack = Stack()
stack.push('data1')
stack.push('data2')
stack.push('data3')

print(stack.top.data)
print(stack.top.next_node.data)
print(stack.top.next_node.next_node.data)
print(stack.top.next_node.next_node.next_node)
print(stack.top.next_node.next_node.next_node.data)

