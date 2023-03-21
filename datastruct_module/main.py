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




