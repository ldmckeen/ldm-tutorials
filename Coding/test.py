class Node:
    
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    
    # Function to initialize head
    def __init__(self):
        self.head = None
    
    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    # Given a reference to the head of a list and a key,
    # delete the first occurrence of key in linked list
    def deleteNode(self, key):
        
        # Store head node
        temp = self.head
        
        # If head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
        
        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        
        # if key was not present in linked list
        if (temp == None):
            return
        
        # Unlink the node from linked list
        prev.next = temp.next
        
        temp = None
    
    # Utility function to print the linked LinkedList
    
    def printList(self):
        temp = self.head
        while (temp):
            print(" %d" % (temp.data)),
            temp = temp.next


def deleteListNode(listHead, key):
    # Store head node
    temp = listHead.head
    
    # If head node itself holds the key to be deleted
    if temp is not None:
        if temp.data == key:
            listHead.head = temp.next
            temp = None
    
    prev = temp
    # Search for the key to be deleted, keep track of the
    # previous node as we need to change 'prev.next'
    # while temp is not None:
    #     if temp.data > key:
    #         break
    #     prev = temp
    #     temp = temp.next
    
    while temp is not None:
        while temp is not None and temp.data <= key:
            prev = temp
            temp = temp.next
        if temp == None:
            return temp
        prev.next = temp.next
        temp = prev.next
    
    # if key was not present in linked list
    # if temp == None:
    #     return temp
    #
    # # Unlink the node from linked list
    # prev.next = temp.next
    
    return temp


"""
// nodes other than head having value greater than x
        while (temp != null) {
            while (temp != null && temp.data <= x) {
                prev = temp;
                temp = temp.next;
            }
            if (temp == null) {
                return head;
            }
            // if there is a node in middle which has
            // greater value, we point the node to the next
            // node.
            prev.next = temp.next;
            // update temp for next iteration of loop.
            temp = prev.next;
        }
        return head;
"""


def deleteListNodes(listHead, key):
    temp = listHead.head


if __name__ == '__main__':
    # Driver program
    llist = LinkedList()
    llist.push(7)
    llist.push(3)
    llist.push(4)
    llist.push(8)
    llist.push(5)
    llist.push(1)
    
    print("Created Linked List: ")
    llist.printList()
    # llist.deleteNode(1)
    
    result = deleteListNodes(llist, 1)
    print("\nLinked List after Deletion of 1:")
    llist.printList()
    # print(result)
