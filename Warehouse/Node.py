class Node:
    def __init__(self, name = None, next = None, previous = None):
        self.name = name
        self.next = next
        self.previous = previous

    def __str__(self):
        return str(self.name)
