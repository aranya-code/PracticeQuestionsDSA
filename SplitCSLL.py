"""

Split a Circular Linked List into Two Equal Halves

Write a function to split the circular linked list into two equal halves. 
If the list has odd number of nodes, the extra node should go to the first list. 

"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:  # Stop condition for circular list
                break
            result += ' -> '
        return result

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def split_list(self):
        # TODO
        if self.length == 0:
            return None, None
        
        if self.length == 1:
            first_list = CSLinkedList()
            return first_list, None
        
        slow = fast = self.head
        
        while fast.next != self.head and fast.next.next != self.head:
            slow = slow.next
            fast = fast.next.next
        
        if fast.next.next == self.head:
            fast = fast.next
        
        head1 = self.head
        head2 = slow.next
        
        slow.next = head1
        fast.next = head2
        
        
        first_list = CSLinkedList()
        temp = head1
        
        while True:
            first_list.append(temp.value)
            temp = temp.next
            
            if temp == head1:
                break
        
        second_list = CSLinkedList()
        temp = head2
        
        while True:
            second_list.append(temp.value)
            temp = temp.next
            
            if temp == head2:
                break
            
        
        
        

        return first_list, second_list


