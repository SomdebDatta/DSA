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
        while current_node and position != index:
            current_node = current_node.next
            position += 1
        if current_node:
            rem_node = current_node.next
            current_node.next = rem_node.next
            rem_node.next = None

    def printLinkedList(self):
        current_node = self.head
        while current_node:
            print(f"Value of current node - {current_node.data}")
            current_node = current_node.next


my_linked_list = LinkedList()
my_linked_list.insertAtBegin(1)
my_linked_list.insertAtEnd(2)
my_linked_list.insertAtEnd(3)
my_linked_list.insertAtEnd(4)
my_linked_list.printLinkedList()
