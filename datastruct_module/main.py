from datastruct_module.custom_queue import Queue
from datastruct_module.linked_list import LinkedList
from datastruct_module.stack import Stack

if __name__ == '__main__':
    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    stack.push('data3')

    print(stack.top.data)
    print(stack.top.next_node.data)
    print(stack.top.next_node.next_node.data)
    print(stack.top.next_node.next_node.next_node)
    # print(stack.top.next_node.next_node.next_node.data)

    print()

    data = stack.pop()
    print(stack.top.data)
    print(data)
    print()

    data = stack.pop()
    print(stack.top.data)
    print(data)

    print()
    data = stack.pop()
    print(stack.top)
    print(data)


    ll = LinkedList()
    ll.insert_beginning({'id': 1})
    ll.insert_at_end({'id': 2})
    ll.insert_at_end({'id': 3})
    ll.insert_beginning({'id': 0})
    ll.print_ll()
    # {'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None
    # print()
    # data = stack.pop()
    # print(stack.top)

    # queue = Queue()
    # queue.enqueue('data1')
    # queue.enqueue('data2')
    # queue.enqueue('data3')
    #
    # print()
    # print("queue")
    # print(queue.head.data)
    # print(queue.head.next_node.data)
    # print(queue.tail.data)
    # print(queue.tail.next_node)
    # # print(queue.tail.next_node.data)

    # print()
    # print('----------------------------------------------------------------------------------------------')
    # queue1 = Queue()
    # queue1.enqueue('data1')
    # queue1.enqueue('data2')
    # queue1.enqueue('data3')
    #
    # print(queue1.dequeue())  # data1
    #
    # print(queue1.dequeue())  # data2
    # #
    # print(queue1.dequeue())  # data3
    # #
    # print(queue1.dequeue())  # None
