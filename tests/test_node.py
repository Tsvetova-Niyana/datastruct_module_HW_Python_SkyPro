import unittest
from datastruct_module.Node import Node


class TestNode(unittest.TestCase):
    """Тест класса Node"""

    def test_check_node_at_init_node_without_node_next(self):
        """Проверка корректной инициализации класса Node:
             с атрибутом data
             без атрибута next_node"""
        node = Node('test')

        assert node.data == 'test'

    def test_check_node_text_at_init_node_without_node_next(self):
        """Проверка корректной инициализации класса Node:
             с атрибутом data
             без атрибута next_node"""
        node = Node('test')

        assert node.next_node is None

    def test_check_node_at_init_node_with_node_next(self):
        """Проверка корректной инициализации класса Node:
             c атрибутом data
             c атрибутом next_node"""
        node = Node('test', 'node')

        assert node.data == 'test'

    def test_check_node_next_at_init_node_with_node_next(self):
        """Проверка корректной инициализации класса Node:
             c атрибутом data
             c атрибутом next_node"""
        node = Node('test', 'node')

        assert node.next_node == 'node'

    def test_node_next_in_node(self):
        """Проверка корректной работы атрибута next_node при создании экземпляра класса Node c ссылкой
            на предыдущий узел в атрибуте next_node"""
        node = Node('test')
        node2 = Node('node2', node)

        assert node2.next_node is node

    def test_init_node_without_parameters(self):
        """Проверка вывода ошибки при инициализации класса Node без указания атрибутов"""
        with self.assertRaises(TypeError):
            node = Node()
