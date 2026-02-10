"""
Implement an algorithm to find the nth to last element of a singly linked list

Example:
A->B->C->D->E
node: A
nth: 3
result: C

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

def nth_last_element(node, nth):

"""


class ListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


def nth_last_element(node, nth):
    fast = node
    slow = node
    
    for _ in range(nth):
        if not fast:
            return None
        fast = fast.next
    
    while fast:
        slow = slow.next
        fast = fast.next
        
    return slow.data


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        
    def push(self, new_data):
        new_node = SinglyLinkedListNode(new_data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        
    def push_beginning(self, new_data):
        new_node = SinglyLinkedListNode(new_data)
        new_node.next = self.head
        self.head = new_node
        
    def delete(self, key):
        temp = self.head
        prev = None
        
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
            
        if temp is None:
            return
        
        prev.next = temp.next
        temp = None
    
    def print_list(self):
        temp = self.head
        elements = []
        while temp:
            elements.append(str(temp.data))
            temp = temp.next
        print("->".join(elements) + "->None")
    
    def nth_last_element(self, node, nth):
        fast_pointer = node
        slow_pointer = node
        
        # 1. Move fast pointer n steps ahead
        for _ in range(nth):
            if fast_pointer is None:
                return None  # n is larger than the list length
            fast_pointer = fast_pointer.next
            
        while fast_pointer:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next
        
        return slow_pointer.data if slow_pointer else None

if __name__ == '__main__':
    print("Singly Linked List Class:")
    sll = SinglyLinkedList()
    sll.push('A')
    sll.push('B')
    sll.push('C')
    sll.push('D')
    sll.push('E')
    sll.push('F')
    
    sll.print_list()
    # print("After Delete")
    # sll.delete('C')
    # sll.print_list()
    
    print(sll.nth_last_element(sll.head.next, 3))
    
    print("\nSingly Linked List Node Class")
    a = ListNode("A")
    b = ListNode("B")
    c = ListNode("C")
    d = ListNode("D")
    e = ListNode("E")
    f = ListNode("F")
    
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    
    print(nth_last_element(c, 4))
    
    
    
    
    
    