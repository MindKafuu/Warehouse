class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, node):
        if self.head == None:
            self.head = node
        else:
            n = self.head
            while (n.next != None) :
                n = n.next
            n.next = node
            
    def delete(self, node):
        try:
            if self.head == None:
                return None
            else:
                n = self.head
                if n.name == node.name:
                    self.head = n.previous
                else:
                    while(n.next.name != node.name):
                        try:
                            n = n.next
                        except AttributeError:
                            pass
                    n.next = n.previous
        except AttributeError:
            pass
                
    def search(self, node):
        if self.head == None:
            return None
        else:
            n = self.head
            while (n.name != node.name):
                try:
                    n = n.next
                except AttributeError:
                    pass
            return n
       
    def __str__(self):
        s = ""
        n = self.head
        while (n != None) :
            s = s + n.name
            n = n.next

        return s
            
