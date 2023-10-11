class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtBegin(new_node)
        else:
            while current_node and position + 1 != index:
                current_node = current_node.next
                position += 1

            if current_node:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Invalid index!")

    def insertAtEnd(self, data):
        new_node = Node(data)
        if not self.head:
            self.insertAtBegin(new_node)
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next

            current_node.next = new_node

    def remove_first_node(self):
        if self.head:
            self.head = self.head.next
        return

    def remove_last_node(self):
        if not self.head:
            return
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next

        current_node.next = None

    def remove_node(self, index):
        if index == 0:
            self.remove_first_node()
            return

        position = 0
        current_node = self.head
        while current_node and position + 1 != index:
            current_node = current_node.next
            position += 1
        if current_node.next.data:
            current_node.next = current_node.next.next

    def printLinkedList(self):
        current_node = self.head
        print("Linked list -> ", end=" ")
        while current_node:
            print(f"{current_node.data}", end=" ")
            current_node = current_node.next
        print()

    def length(self):
        n = 0
        if not self.head:
            return n
        else:
            current_node = self.head
            while current_node:
                current_node = current_node.next
                n += 1
            return n


print("Creating and adding values to the Linked List")
my_linked_list = LinkedList()
my_linked_list.insertAtBegin(1)
my_linked_list.insertAtEnd(2)
my_linked_list.insertAtEnd(3)
my_linked_list.insertAtBegin(4)
my_linked_list.printLinkedList()

print("Now removing first node")
my_linked_list.remove_first_node()
my_linked_list.printLinkedList()


print("Now removing last node")
my_linked_list.remove_last_node()
my_linked_list.printLinkedList()


print("Adding value in the middle")
my_linked_list.insertAtIndex(5, 1)
my_linked_list.printLinkedList()


print("Adding value in the middle")
my_linked_list.insertAtIndex(99, 1)
my_linked_list.printLinkedList()


print("Removing value from the middle")
my_linked_list.remove_node(1)
my_linked_list.printLinkedList()

print("Calculating length of the Linked List.")
print(f"Length - {my_linked_list.length()}")
