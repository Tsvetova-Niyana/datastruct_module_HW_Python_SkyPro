"""
Реализуйте структуру односвязанный список.

Создайте файл `linked_list.py` и в нем два класса: `Node` и `LinkedList`.

- Класс `Node` хранит полезные данные (словарь с данными) и ссылку на следующий узел
- Класс `LinkedList` хранит ссылку на начало связанного списка и на его конец, т.е. на первый и последний `Node`.
- Реализуйте две метода у класса `LinkedList`:
    - `insert_beginning` - принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка
    - `insert_at_end` - принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка
- Используйте следующий метод для вывода в консоль данных из односвязанного списка:
 def print_ll(self):
        ll_string = ''
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        print(ll_string)
"""

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data: list):

        node_new = Node(data)

        if self.head is None:
            self.head = node_new
            self.tail = node_new
        else:
            node_new.next_node = self.head
            self.head = node_new

    def insert_at_end(self, data: list):

        node_new = Node(data)

        if self.head is None:
            self.head = node_new
            self.tail = node_new
        else:
            self.tail.next_node = node_new
            self.tail = node_new
