import unittest
from datastruct_module.custom_queue import Queue


class TestQueue(unittest.TestCase):
    """Тест класса Queue"""

    def test_check_head_init(self):
        """Проверка свойства queue.head при инициализации класса Queue"""
        queue = Queue()

        assert queue.head is None

    def test_check_tail_init(self):
        """Проверка свойства queue.tail при инициализации класса Queue"""
        queue = Queue()

        assert queue.tail is None

    def test_check_head_data_add_one_node_in_queue(self):
        """Проверка корректности работы метода enqueue при передаче одного узла (атрибут head.data)"""
        queue = Queue()
        queue.enqueue('test')

        assert queue.head.data == 'test'

    def test_check_tail_data_add_one_node_in_queue(self):
        """Проверка корректности работы метода enqueue при передаче одного узла (атрибут tail.data)"""
        queue = Queue()
        queue.enqueue('test')

        assert queue.tail.data == 'test'

    def testcheck_head_data_add_two_node_in_queue(self):
        """Проверка корректности работы метода enqueue при передаче двух узлов (атрибут head.data)"""
        queue = Queue()
        queue.enqueue('test1')
        queue.enqueue('test2')

        assert queue.head.data == 'test1'

    def testcheck_tail_data_add_two_node_in_queue(self):
        """Проверка корректности работы метода enqueue при передаче двух узлов (атрибут head.data)"""
        queue = Queue()
        queue.enqueue('test1')
        queue.enqueue('test2')

        assert queue.tail.data == 'test2'

    def test_check_head_next_node_data_add_two_node_in_queue(self):
        """Проверка корректности работы метода enqueue при передаче двух узлов (атрибут head.next_node.data)"""
        queue = Queue()
        queue.enqueue('test1')
        queue.enqueue('test2')

        assert queue.head.next_node.data == 'test2'

    def test_check_tail_next_node_data_add_two_node_in_queue(self):
        """Проверка корректности работы метода enqueue при передаче двух узлов (атрибут tail.next_node)"""
        queue = Queue()
        queue.enqueue('test1')
        queue.enqueue('test2')

        assert queue.tail.next_node is None

    def test_check_raise_two_node_in_queue(self):
        """Проверка вывода ошибки при попытке получения информации из атрибута tail.next_node.data нулевого уровня"""
        queue = Queue()
        queue.enqueue('test1')
        queue.enqueue('test2')

        with self.assertRaises(AttributeError):
            queue.tail.next_node.data

    def testcheck_head_data_add_many_node_in_queue(self):
        """Проверка корректности работы метода enqueue при передаче двух узлов (атрибут head.data)"""
        queue = Queue()
        queue.enqueue('test1')
        queue.enqueue('test2')
        queue.enqueue('test3')

        assert queue.head.data == 'test1'

    def testcheck_tail_data_add_many_node_in_queue(self):
        """Проверка корректности работы метода enqueue при передаче двух узлов (атрибут head.data)"""
        queue = Queue()
        queue.enqueue('test1')
        queue.enqueue('test2')
        queue.enqueue('test3')

        assert queue.tail.data == 'test3'

    def test_check_head_next_node_data_many_node_in_queue(self):
        """Проверка корректности работы метода enqueue при передаче двух узлов (атрибут head.next_node.data)"""
        queue = Queue()
        queue.enqueue('test1')
        queue.enqueue('test2')
        queue.enqueue('test3')

        assert queue.head.next_node.data == 'test2'

    def test_check_head_next_node_data_many_two_node_in_queue(self):
        """Проверка корректности работы метода enqueue при передаче двух узлов (атрибут head.next_node.data)"""
        queue = Queue()
        queue.enqueue('test1')
        queue.enqueue('test2')
        queue.enqueue('test3')

        assert queue.head.next_node.next_node.data == 'test3'

    def test_check_tail_next_node_data_add_many_node_in_queue(self):
        """Проверка корректности работы метода enqueue при передаче двух узлов (атрибут tail.next_node)"""
        queue = Queue()
        queue.enqueue('test1')
        queue.enqueue('test2')
        queue.enqueue('test3')

        assert queue.tail.next_node is None

    def test_check_raise_many_node_in_queue(self):
        """Проверка вывода ошибки при попытке получения информации из атрибута tail.next_node.data нулевого уровня"""
        queue = Queue()
        queue.enqueue('test1')
        queue.enqueue('test2')
        queue.enqueue('test3')

        with self.assertRaises(AttributeError):
            queue.tail.next_node.data
