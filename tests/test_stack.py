import unittest
from datastruct_module.Stack import Stack


class TestStack(unittest.TestCase):
    """Тест класса Stack"""
    def test_init_stack_without_parameters(self):
        """Проверка инициализации класса Stack без явной передачи атрибутов"""
        stack = Stack()

        assert stack.top is None

    def test_init_stack_with_parameters(self):
        """Проверка инициализации класса Stack с явной передачей атрибутов"""
        stack = Stack('test')

        assert stack.top == 'test'

    def test_check_stack_top_data_push_in_stack_one(self):
        """Проверка корректности работы метода push при передаче одного узла (атрибут top.data)"""
        stack = Stack()
        stack.push('test')

        assert stack.top.data == 'test'

    def test_check_stack_top_next_node_push_in_stack_one(self):
        """Проверка корректности работы метода push при передаче одного узла (атрибут top.next_node)"""
        stack = Stack()
        stack.push('test')

        assert stack.top.next_node is None

    def test_check_stack_top_data_push_in_stack_two(self):
        """Проверка корректности работы метода push при передаче двух узлов (атрибут top.data)"""
        stack = Stack()
        stack.push('test')
        stack.push('test2')

        assert stack.top.data == 'test2'

    def test_check_next_node__node_one_level_back_push_in_stack_two(self):
        """Проверка корректности работы метода push при передаче двух узлов
            (атрибут next_node.data - предыдущий уровень)"""
        stack = Stack()
        stack.push('test')
        stack.push('test2')

        assert stack.top.next_node.data == 'test'

    def test_check_stack_top_data_push_in_stack_many(self):
        """Проверка корректности работы метода push при передаче нескольких узлов (атрибут top.data)"""
        stack = Stack()
        stack.push('test')
        stack.push('test2')
        stack.push('test3')

        assert stack.top.data == 'test3'

    def test_check_next_node_one_level_back_push_in_stack_many(self):
        """Проверка корректности работы метода push при передаче нескольких узлов
            (первый уровень)"""
        stack = Stack()
        stack.push('test')
        stack.push('test2')
        stack.push('test3')

        assert stack.top.next_node.data == 'test2'

    def test_check_next_node_two_level_push_in_stack_many(self):
        """Проверка корректности работы метода push при передаче нескольких узлов
            (второй уровень)"""
        stack = Stack()
        stack.push('test')
        stack.push('test2')
        stack.push('test3')

        assert stack.top.next_node.next_node.data == 'test'

    def test_check_stack_top_next_node_none_push_in_stack_many(self):
        """Проверка корректности работы метода push при передаче нескольких узлов
            (нулевой уровень)"""
        stack = Stack()
        stack.push('test')
        stack.push('test2')
        stack.push('test3')

        assert stack.top.next_node.next_node.next_node is None

    def test_check_raise_push_in_stack_many(self):
        stack = Stack()
        stack.push('test')
        stack.push('test2')
        stack.push('test3')

        with self.assertRaises(AttributeError):
            """Проверка вывода ошибки при попытке получения информации из атрибута next_node.data нулевого уровня"""
            stack.top.next_node.next_node.next_node.data
