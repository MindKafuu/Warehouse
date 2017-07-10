class HashTable:
    def __init__(self):
        self.hash = [None] * 5

    def hash_function(self, data):
        s = 0
        for pos in range(len(data)):
            s = s + ord(data[pos])
        return s % 5

    def add(self, key, value):
        key = self.hash_function(key)
        while (self.hash[key] != None):
            key = self.hash_function(key)
            self.hash[key] = value
        key = self.hash_function(key)
        self.hash[key] = value

    def delete(self,key):
        key = self.hashfunction(key)
        self.hash[key] = None

    def _print(self):
        s = ""
        for i in self.hash:
            if i != None:
                s = s + str(i) + " "
            else:
                pass
        return s
    
    def __str__(self):
        return str(self.hash)

h = HashTable()
h.add("apple", 55)
h.add("apple", 44)
h.add("apple", 33)



print(h)


