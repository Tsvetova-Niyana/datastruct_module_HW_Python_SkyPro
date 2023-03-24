from datastruct_module.custom_queue import Queue
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

    queue = Queue()
    queue.enqueue('data1')
    queue.enqueue('data2')
    queue.enqueue('data3')

    print()
    print("queue")
    print(queue.head.data)
    print(queue.head.next_node.data)
    print(queue.tail.data)
    print(queue.tail.next_node)
    # print(queue.tail.next_node.data)

    print()
    print('----------------------------------------------------------------------------------------------')
    queue1 = Queue()
    queue1.enqueue('data1')
    queue1.enqueue('data2')
    queue1.enqueue('data3')

    print(queue1.dequeue())  # data1

    print(queue1.dequeue())  # data2
    #
    print(queue1.dequeue())  # data3
    #
    print(queue1.dequeue())  # None
