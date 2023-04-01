import unittest
from datastruct_module.linked_list import Node, LinkedList


class TestLinkedList(unittest.TestCase):
    def test_init_linked_list(self):
        ll = LinkedList()
        assert ll is not None

    def test_init_head_linked_list(self):
        ll = LinkedList()
        assert ll.head is None

    def test_init_tail_linked_list(self):
        ll = LinkedList()
        assert ll.tail is None

    def test_check_head_insert_beginning_one_node_linked_list(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        assert str(ll.head.data) == "{'id': 1}"

    def test_check_tail_insert_beginning_one_node_linked_list(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        assert str(ll.tail.data) == "{'id': 1}"

    def test_check_head_insert_beginning_two_node(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        ll.insert_beginning({'id': 0})
        assert str(ll.head.data) == "{'id': 0}"

    def test_check_tail_insert_beginning_two_node(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        ll.insert_beginning({'id': 0})
        assert str(ll.tail.data) == "{'id': 1}"

    def test_check_head_insert_at_end_one_node_linked_list(self):
        ll = LinkedList()
        ll.insert_at_end({'id': 2})
        assert str(ll.head.data) == "{'id': 2}"

    def test_check_tail_insert_at_end_one_node_linked_list(self):
        ll = LinkedList()
        ll.insert_at_end({'id': 2})
        assert str(ll.tail.data) == "{'id': 2}"

    def test_check_head_insert_at_end_two_node(self):
        ll = LinkedList()
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        assert str(ll.head.data) == "{'id': 2}"

    def test_check_tail_insert_at_end_two_node(self):
        ll = LinkedList()
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        assert str(ll.tail.data) == "{'id': 3}"

    def test_check_head_insert_mix_node(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        ll.insert_beginning({'id': 0})
        assert str(ll.head.data) == "{'id': 0}"

    def test_check_tail_insert_mix_two_node(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        ll.insert_beginning({'id': 0})
        assert str(ll.tail.data) == "{'id': 3}"

    def test_check_print_ll_with_node(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        ll.insert_beginning({'id': 0})
        assert str(ll.print_ll) is not None

    class TestNode(unittest.TestCase):
        def test_check_node_at_init_node_without_node_next(self):
            """Проверка корректной инициализации класса Node:
                 с атрибутом data
                 без атрибута next_node"""
            node = Node({'id': 1})

            assert node.data == "{'id': 1}"

        def test_check_node_text_at_init_node_without_node_next(self):
            """Проверка корректной инициализации класса Node:
                 с атрибутом data
                 без атрибута next_node"""
            node = Node({'id': 1})

            assert node.next_node is None

