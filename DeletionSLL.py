class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def remove(self, index):
        if self.head is None or index < 0 or index >= self.length:
            return None

        # Remove head
        if index == 0:
            popped_node = self.head
            self.head = self.head.next

            if self.length == 1:
                self.tail = None

            popped_node.next = None
            self.length -= 1
            return popped_node

        # Remove middle or tail
        prev_node = self.get(index - 1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next

        if index == self.length - 1:
            self.tail = prev_node

        popped_node.next = None
        self.length -= 1
        return popped_node
