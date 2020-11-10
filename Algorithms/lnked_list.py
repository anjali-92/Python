class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None

    def add_element(self, node):
        if self.head == None:
            self.head = node
            return
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = node

    def remove_element(self, value):
        if self.head == None:
            return

        if self.head.value == value:
            if self.head.next:
                self.head = self.head.next
            else:
                self.head = None
            return

        prev = temp = self.head
        while temp != None:
            if temp.value == value:
                prev.next = temp.next
                break
            prev = temp
            temp = temp.next

    def print_ll(self):
        if self.head == None:
            return None
        temp = self.head
        l = []
        while temp != None:
            l.append(temp.value)
            temp = temp.next
        print(l)

if __name__ == "__main__":
    node = Node(10)
    ll = LinkedList()
    ll.add_element(node)
    ll.print_ll()
    
    node = Node(20)
    ll.add_element(node)
    ll.print_ll()
    
    ll.remove_element(20)
    ll.print_ll()

    ll.remove_element(10)
    ll.print_ll()