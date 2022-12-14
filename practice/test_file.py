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


def deleteListNode(listHead, x):
    # Write your code here
    current_node = listHead.head
    while current_node is not None and current_node.data > x:
        current_node = current_node.next
        listHead = current_node

    current_node = listHead.head
    previous_node = current_node

    while current_node is not None:

        while current_node is not None and current_node.data <= x:
            previous_node = current_node
            current_node = current_node.next

        if current_node == None:
            return listHead.head
        previous_node.next = current_node.next
        current_node = previous_node.next

    return listHead.head

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

    result = deleteListNode(llist, 5)
    print("\nLinked List after Deletion of 1:")
    llist.printList()
    # print(result)
