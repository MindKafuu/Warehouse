from Node import Node

class queue:
    def __init__(self):
        a = Node()
        self.head = a
        self.size = 0

    def add(self, node):
        if self.size < 10:
            n = self.head
            while (n.next != None) :
                 n = n.next
            n.next = node
            self.size = self.size + 1

    def remove(self):
        n = (self.head).next
        (self.head).next = ((self.head).next).next
        self.size = self.size - 1
        return n
        
    def __str__(self):
        s = ""
        n = self.head.next
        while (n != None):
            s = s + n.name + " "
            n = n.next

        return s
        
