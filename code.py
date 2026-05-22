# A linked list node
class Node:
    def __init__(self, newData):
        # Constructor to initialize a new node with data
        self.data = newData
        self.next = None

# Function to print the singly linked list
def printList(node):
    while node is not None:
        print(f"{node.data}", end="")
        if node.next is not None:
            print("->", end="")
        node = node.next
    print()


if __name__ == "__main__":

    # Create a linked list: 10 -> 20 -> 30 -> 40
    print("LINKED LIST:")
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)

    printList(head)