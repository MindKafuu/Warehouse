from Node import Node
from queue import queue
from bubbleSort import bubbleSort
from bubble_Sort import bubble_Sort

belt = queue()

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count = 0

s1 = ""
s2 = ""
s3 = ""
s4 = ""
s5 = ""

class WareHouse3:
    def __init__(self):
        self.Arow1 = [[None] * 10 for i in range(10)]
        self.Arow2 = [[None] * 10 for i in range(10)]
        self.Arow3 = [[None] * 10 for i in range(10)]
        self.Arow4 = [[None] * 8 for i in range(8)]
        self.Arow5 = [[None] * 8 for i in range(8)]

        self.Brow1 = [[None] * 10 for i in range(10)]
        self.Brow2 = [[None] * 10 for i in range(10)]
        self.Brow3 = [[None] * 10 for i in range(10)]
        self.Brow4 = [[None] * 8 for i in range(8)]
        self.Brow5 = [[None] * 8 for i in range(8)]

        self.Crow1 = [[None] * 10 for i in range(10)]
        self.Crow2 = [[None] * 10 for i in range(10)]
        self.Crow3 = [[None] * 10 for i in range(10)]
        self.Crow4 = [[None] * 8 for i in range(8)]
        self.Crow5 = [[None] * 8 for i in range(8)]

        self.Drow1 = [[None] * 10 for i in range(10)]
        self.Drow2 = [[None] * 10 for i in range(10)]
        self.Drow3 = [[None] * 10 for i in range(10)]
        self.Drow4 = [[None] * 8 for i in range(8)]
        self.Drow5 = [[None] * 8 for i in range(8)]

        self.Erow1 = [[None] * 10 for i in range(10)]
        self.Erow2 = [[None] * 10 for i in range(10)]
        self.Erow3 = [[None] * 10 for i in range(10)]
        self.Erow4 = [[None] * 8 for i in range(8)]
        self.Erow5 = [[None] * 8 for i in range(8)]


    def num0(self, row, x, y, kind):
        if kind == "A":
            if row == "1":
                if belt.size < 10:
                    if self.Arow1[x][y] != None:
                        belt.add(Node(str(self.Arow1[x][y])))
                        self.Arow1[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Arow1)
            elif row == "2":
                if belt.size < 10:
                    if self.Arow2[x][y] != None:
                        belt.add(Node(str(self.Arow2[x][y])))
                        self.Arow2[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Arow2)
            elif row == "3":
                if belt.size < 10:
                    if self.Arow3[x][y] != None:
                        belt.add(Node(str(self.Arow3[x][y])))
                        self.Arow3[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Arow3)
            elif row == "4":
                if belt.size < 10:
                    if self.Arow4[x][y] != None:
                        belt.add(Node(str(self.Arow4[x][y])))
                        self.Arow4[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Arow4)
            elif row == "5":
                if belt.size < 10:
                    if self.Arow5[x][y] != None:
                        belt.add(Node(str(self.Arow5[x][y])))
                        self.Arow5[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Arow5)
        elif kind == "B":
            if row == "1":
                if belt.size < 10:
                    if self.Brow1[x][y] != None:
                        belt.add(Node(str(self.Brow1[x][y])))
                        self.Brow1[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Brow1)
            elif row == "2":
                if belt.size < 10:
                    if self.Brow2[x][y] != None:
                        belt.add(Node(str(self.Brow2[x][y])))
                        self.Brow2[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Brow2)
            elif row == "3":
                if belt.size < 10:
                    if self.Brow3[x][y] != None:
                        belt.add(Node(str(self.Brow3[x][y])))
                        self.Brow3[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Brow3)
            elif row == "4":
                if belt.size < 10:
                    if self.Brow4[x][y] != None:
                        belt.add(Node(str(self.Brow4[x][y])))
                        self.Brow4[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Brow4)
            elif row == "5":
                if belt.size < 10:
                    if self.Brow5[x][y] != None:
                        belt.add(Node(str(self.Brow5[x][y])))
                        self.Brow5[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Brow5)
        elif kind == "C":
            if row == "1":
                if belt.size < 10:
                    if self.Crow1[x][y] != None:
                        belt.add(Node(str(self.Crow1[x][y])))
                        self.Crow1[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Crow1)
            elif row == "2":
                if belt.size < 10:
                    if self.Crow2[x][y] != None:
                        belt.add(Node(str(self.Crow2[x][y])))
                        self.Crow2[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Crow2)
            elif row == "3":
                if belt.size < 10:
                    if self.Crow3[x][y] != None:
                        belt.add(Node(str(self.Crow3[x][y])))
                        self.Crow3[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Crow3)
            elif row == "4":
                if belt.size < 10:
                    if self.Crow4[x][y] != None:
                        belt.add(Node(str(self.Crow4[x][y])))
                        self.Crow4[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Crow4)
            elif row == "5":
                if belt.size < 10:
                    if self.Crow5[x][y] != None:
                        belt.add(Node(str(self.Crow5[x][y])))
                        self.Crow5[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Crow5)
        elif kind == "D":
            if row == "1":
                if belt.size < 10:
                    if self.Drow1[x][y] != None:
                        belt.add(Node(str(self.Drow1[x][y])))
                        self.Drow1[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Drow1)
            elif row == "2":
                if belt.size < 10:
                    if self.Drow2[x][y] != None:
                        belt.add(Node(str(self.Drow2[x][y])))
                        self.Drow2[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Drow2)
            elif row == "3":
                if belt.size < 10:
                    if self.Drow3[x][y] != None:
                        belt.add(Node(str(selfD.row3[x][y])))
                        self.Drow3[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Drow3)
            elif row == "4":
                if belt.size < 10:
                    if self.Drow4[x][y] != None:
                        belt.add(Node(str(self.Drow4[x][y])))
                        self.Drow4[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Drow4)
            elif row == "5":
                if belt.size < 10:
                    if self.Drow5[x][y] != None:
                        belt.add(Node(str(self.Drow5[x][y])))
                        self.Drow5[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Drow5)
        elif kind == "E":
            if row == "1":
                if belt.size < 10:
                    if self.Erow1[x][y] != None:
                        belt.add(Node(str(self.Erow1[x][y])))
                        self.Erow1[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Erow1)
            elif row == "2":
                if belt.size < 10:
                    if self.Erow2[x][y] != None:
                        belt.add(Node(str(self.Erow2[x][y])))
                        self.Erow2[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Erow2)
            elif row == "3":
                if belt.size < 10:
                    if self.Erow3[x][y] != None:
                        belt.add(Node(str(self.Erow3[x][y])))
                        self.Erow3[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Erow3)
            elif row == "4":
                if belt.size < 10:
                    if self.Erow4[x][y] != None:
                        belt.add(Node(str(self.Erow4[x][y])))
                        self.Erow4[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Erow4)
            elif row == "5":
                if belt.size < 10:
                    if self.Erow5[x][y] != None:
                        belt.add(Node(str(self.Erow5[x][y])))
                        self.Erow5[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Erow5)

    def num1(self, row, x, y, item, kind):
        if kind == "A":
            if row == "1":
                if self.Arow1[x][y] == None:
                    self.Arow1[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Arow1)
            elif row == "2":
                if self.Arow2[x][y] == None:
                    self.Arow2[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Arow2)
            elif row == "3":
                if self.Arow3[x][y] == None:
                    self.Arow3[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Arow3)
            elif row == "4":
                if self.Arow4[x][y] == None:
                    self.Arow4[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Arow4)
            elif row == "5":
                if self.Arow5[x][y] == None:
                    self.Arow5[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Arow5)
        elif kind == "B":
            if row == "1":
                if self.Brow1[x][y] == None:
                    self.Brow1[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Brow1)
            elif row == "2":
                if self.Brow2[x][y] == None:
                    self.Brow2[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Brow2)
            elif row == "3":
                if self.Brow3[x][y] == None:
                    self.Brow3[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Brow3)
            elif row == "4":
                if self.Brow4[x][y] == None:
                    self.Brow4[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Brow4)
            elif row == "5":
                if self.Brow5[x][y] == None:
                    self.Brow5[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Brow5)
        elif kind == "C":
            if row == "1":
                if self.Crow1[x][y] == None:
                    self.Crow1[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Crow1)
            elif row == "2":
                if self.Crow2[x][y] == None:
                    self.Crow2[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Crow2)
            elif row == "3":
                if self.Crow3[x][y] == None:
                    self.Crow3[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Crow3)
            elif row == "4":
                if self.Crow4[x][y] == None:
                    self.Crow4[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Crow4)
            elif row == "5":
                if self.Crow5[x][y] == None:
                    self.Crow5[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Crow5)
        elif kind == "D":
            if row == "1":
                if self.Drow1[x][y] == None:
                    self.Drow1[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Drow1)
            elif row == "2":
                if self.Drow2[x][y] == None:
                    self.Drow2[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Drow2)
            elif row == "3":
                if self.Drow3[x][y] == None:
                    self.Drow3[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Drow3)
            elif row == "4":
                if self.Drow4[x][y] == None:
                    self.Drow4[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Drow4)
            elif row == "5":
                if self.Drow5[x][y] == None:
                    self.Drow5[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Drow5)
        elif kind == "E":
            if row == "1":
                if self.Erow1[x][y] == None:
                    self.Erow1[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Erow1)
            elif row == "2":
                if self.Erow2[x][y] == None:
                    self.Erow2[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Erow2)
            elif row == "3":
                if self.Erow3[x][y] == None:
                    self.Erow3[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Erow3)
            elif row == "4":
                if self.Erow4[x][y] == None:
                    self.Erow4[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Erow4)
            elif row == "5":
                if self.Erow5[x][y] == None:
                    self.Erow5[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Erow5)

    def num2(self, row, kind): 
        if kind == "A":
            if row == "1":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Arow1))
            elif row == "2":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Arow2))
            elif row == "3":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Arow3))
            elif row == "4":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Arow4))
            elif row == "5":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Arow5))
        elif kind == "B":
            if row == "1":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Brow1))
            elif row == "2":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Brow2))
            elif row == "3":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Brow3))
            elif row == "4":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Brow4))
            elif row == "5":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Brow5))
        elif kind == "C":
            if row == "1":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Crow1))
            elif row == "2":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Crow2))
            elif row == "3":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Crow3))
            elif row == "4":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Crow4))
            elif row == "5":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Crow5))
        elif kind == "D":
            if row == "1":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Drow1))
            elif row == "2":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Drow2))
            elif row == "3":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Drow3))
            elif row == "4":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Drow4))
            elif row == "5":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Drow5))
        elif kind == "E":
            if row == "1":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Erow1))
            elif row == "2":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Erow2))
            elif row == "3":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Erow3))
            elif row == "4":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Erow4))
            elif row == "5":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Erow5))

    def num3(self):
        if belt.size != 0:
            belt.remove()
            print("Retrieve a product with id " + str(belt) + " from the belt.")
            print("The belt now has " + str(belt.size) + " products on the line.")
        else:
            print("The belt is empty. Cannot retrieve the product from the belt.")

    def num4(self, ware):
        print("Warehouse: " + ware)
        print("Numbers of Rows: 5")
        self._num4(count, count1, count2, count3, count4, count5, s1, s2, s3, s4, s5)

    def _num4(self, count, count1, count2, count3, count4, count5, s1, s2, s3, s4, s5):
        for i in self.Arow1:
            for j in i:
                if j != None:
                    count1 = count1 + 1
                    s1 = s1 + j + ", "
                else:
                    pass
        for i in self.Arow2:
            for j in i:
                if j != None:
                    count2 = count2 + 1
                    s2 = s2 + j + ", "
                else:
                    pass
        for i in self.Arow3:
            for j in i:
                if j != None:
                    count3 = count3 + 1
                    s3 = s3 + j + ", "
                else:
                    pass
        for i in self.Arow4:
            for j in i:
                if j != None:
                    count4 = count4 + 1
                    s4 = s4 + j + ", "
                else:
                    pass
        for i in self.Arow5:
            for j in i:
                if j != None:
                    count5 = count5 + 1
                    s5 = s5 + j + ", "
                else:
                    pass
        for i in self.Brow1:
            for j in i:
                if j != None:
                    count1 = count1 + 1
                    s1 = s1 + j + ", "
                else:
                    pass
        for i in self.Brow2:
            for j in i:
                if j != None:
                    count2 = count2 + 1
                    s2 = s2 + j + ", "
                else:
                    pass
        for i in self.Brow3:
            for j in i:
                if j != None:
                    count3 = count3 + 1
                    s3 = s3 + j + ", "
                else:
                    pass
        for i in self.Brow4:
            for j in i:
                if j != None:
                    count4 = count4 + 1
                    s4 = s4 + j + ", "
                else:
                    pass
        for i in self.Brow5:
            for j in i:
                if j != None:
                    count5 = count5 + 1
                    s5 = s5 + j + ", "
                else:
                    pass
        for i in self.Crow1:
            for j in i:
                if j != None:
                    count1 = count1 + 1
                    s1 = s1 + j + ", "
                else:
                    pass
        for i in self.Crow2:
            for j in i:
                if j != None:
                    count2 = count2 + 1
                    s2 = s2 + j + ", "
                else:
                    pass
        for i in self.Crow3:
            for j in i:
                if j != None:
                    count3 = count3 + 1
                    s3 = s3 + j + ", "
                else:
                    pass
        for i in self.Crow4:
            for j in i:
                if j != None:
                    count4 = count4 + 1
                    s4 = s4 + j + ", "
                else:
                    pass
        for i in self.Crow5:
            for j in i:
                if j != None:
                    count5 = count5 + 1
                    s5 = s5 + j + ", "
                else:
                    pass
        for i in self.Drow1:
            for j in i:
                if j != None:
                    count1 = count1 + 1
                    s1 = s1 + j + ", "
                else:
                    pass
        for i in self.Drow2:
            for j in i:
                if j != None:
                    count2 = count2 + 1
                    s2 = s2 + j + ", "
                else:
                    pass
        for i in self.Drow3:
            for j in i:
                if j != None:
                    count3 = count3 + 1
                    s3 = s3 + j + ", "
                else:
                    pass
        for i in self.Drow4:
            for j in i:
                if j != None:
                    count4 = count4 + 1
                    s4 = s4 + j + ", "
                else:
                    pass
        for i in self.Drow5:
            for j in i:
                if j != None:
                    count5 = count5 + 1
                    s5 = s5 + j + ", "
                else:
                    pass
        for i in self.Erow1:
            for j in i:
                if j != None:
                    count1 = count1 + 1
                    s1 = s1 + j + ", "
                else:
                    pass
        for i in self.Erow2:
            for j in i:
                if j != None:
                    count2 = count2 + 1
                    s2 = s2 + j + ", "
                else:
                    pass
        for i in self.Erow3:
            for j in i:
                if j != None:
                    count3 = count3 + 1
                    s3 = s3 + j + ", "
                else:
                    pass
        for i in self.Erow4:
            for j in i:
                if j != None:
                    count4 = count4 + 1
                    s4 = s4 + j + ", "
                else:
                    pass
        for i in self.Erow5:
            for j in i:
                if j != None:
                    count5 = count5 + 1
                    s5 = s5 + j + ", "
                else:
                    pass

        count = count1 + count2 + count3 + count4 + count5
        print("Numbers of total products: " + str(count))
        print("Product in row 1: " + s1)
        print("Product in row 2: " + s2)
        print("Product in row 3: " + s3)
        print("Product in row 4: " + s4)
        print("Product in row 5: " + s5)

    def num5(self, row, x, y, item, kind):
        if kind == "A":
            if row == "1":
                if self.Arow1[x][y] != None:
                    if item == self.Arow1[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
            elif row == "2":
                if self.Arow2[x][y] != None:
                    if item == self.Arow2[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
            elif row == "3":
                if self.Arow3[x][y] != None:
                    if item == self.Arow3[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
            elif row == "4":
                if self.Arow4[x][y] != None:
                    if item == self.Arow4[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
            elif row == "5":
                if self.Arow5[x][y] != None:
                    if item == self.Arow5[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
        if kind == "B":
            if row == "1":
                if self.Brow1[x][y] != None:
                    if item == self.Brow1[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
            elif row == "2":
                if self.Brow2[x][y] != None:
                    if item == self.Brow2[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
            elif row == "3":
                if self.Brow3[x][y] != None:
                    if item == self.Brow3[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
            elif row == "4":
                if self.Brow4[x][y] != None:
                    if item == self.Brow4[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
            elif row == "5":
                if self.Brow5[x][y] != None:
                    if item == self.Brow5[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
        if kind == "C":
            if row == "1":
                if self.Crow1[x][y] != None:
                    if item == self.Crow1[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
            elif row == "2":
                if self.Crow2[x][y] != None:
                    if item == self.Crow2[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
            elif row == "3":
                if self.Crow3[x][y] != None:
                    if item == self.Crow3[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
            elif row == "4":
                if self.Crow4[x][y] != None:
                    if item == self.Crow4[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
            elif row == "5":
                if self.Crow5[x][y] != None:
                    if item == self.Crow5[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
        if kind == "D":
            if row == "1":
                if self.Drow1[x][y] != None:
                    if item == self.Drow1[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
            elif row == "2":
                if self.Drow2[x][y] != None:
                    if item == self.Drow2[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
            elif row == "3":
                if self.Drow3[x][y] != None:
                    if item == self.Drow3[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
            elif row == "4":
                if self.Drow4[x][y] != None:
                    if item == self.Drow4[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
            elif row == "5":
                if self.Drow5[x][y] != None:
                    if item == self.Drow5[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
        if kind == "E":
            if row == "1":
                if self.Erow1[x][y] != None:
                    if item == self.Erow1[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
            elif row == "2":
                if self.Erow2[x][y] != None:
                    if item == self.Erow2[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
            elif row == "3":
                if self.Erow3[x][y] != None:
                    if item == self.Erow3[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
            elif row == "4":
                if self.Erow4[x][y] != None:
                    if item == self.Erow4[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
            elif row == "5":
                if self.Erow5[x][y] != None:
                    if item == self.Erow5[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")

    def num9(self, row, x, y, kind, item, _row, _x, _y, _kind, _item):
        if kind == "A" and _kind == "A":
            if row == "1":
                if self.Arow1[x][y] == None and self.Arow1[_x][_y] == None:
                     print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Arow1[x][y]
                    self.Arow1[x][y] = self.Arow1[_x][_y]
                    self.Arow1[_x][_y] = box
                print(self.Arow1)
            elif row == "2":
                if self.Arow2[x][y] == None and self.Arow2[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Arow1[x][y]
                    self.Arow2[x][y] = self.Arow2[_x][_y]
                    self.Arow2[_x][_y] = box
                print(self.Arow2)
            elif row == "3":
                if self.Arow1[x][y] == None and self.Arow1[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Arow3[x][y]
                    self.Arow3[x][y] = self.Arow3[_x][_y]
                    self.Arow3[_x][_y] = box
                print(self.Arow3)
            elif row == "4":
                if self.Arow4[x][y] == None and self.Arow4[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Arow4[x][y]
                    self.Arow4[x][y] = self.Arow4[_x][_y]
                    self.Arow4[_x][_y] = box
                print(self.Arow4)
            elif row == "5":
                if self.Arow5[x][y] == None and self.Arow5[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Arow5[x][y]
                    self.Arow5[x][y] = self.Arow5[_x][_y]
                    self.Arow5[_x][_y] = box
                    print(sel5.Arow4)
        if kind == "B" and _kind == "B":
            if row == "1":
                if self.Brow1[x][y] == None and self.Brow1[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Brow1[x][y]
                    self.Brow1[x][y] = self.Brow1[_x][_y]
                    self.Brow1[_x][_y] = box
                print(self.Brow1)
            elif row == "2":
                if self.Brow2[x][y] == None and self.Brow2[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Brow1[x][y]
                    self.Brow2[x][y] = self.Brow2[_x][_y]
                    self.Brow2[_x][_y] = box
                print(self.Brow2)
            elif row == "3":
                if self.Brow1[x][y] == None and self.Brow1[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Brow3[x][y]
                    self.Brow3[x][y] = self.Brow3[_x][_y]
                    self.Brow3[_x][_y] = box
                print(self.Brow3)
            elif row == "4":
                if self.Brow4[x][y] == None and self.Brow4[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Brow4[x][y]
                    self.Brow4[x][y] = self.Brow4[_x][_y]
                    self.Brow4[_x][_y] = box
                print(self.Brow4)
            elif row == "5":
                if self.Brow5[x][y] == None and self.Brow5[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Brow5[x][y]
                    self.Brow5[x][y] = self.Brow5[_x][_y]
                    self.Brow5[_x][_y] = box
                    print(sel5.Brow4)
        if kind == "C" and _kind == "C":
            if row == "1":
                if self.Crow1[x][y] == None and self.Crow1[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Crow1[x][y]
                    self.Crow1[x][y] = self.Crow1[_x][_y]
                    self.Crow1[_x][_y] = box
                print(self.Crow1)
            elif row == "2":
                if self.Crow2[x][y] == None and self.Crow2[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Crow1[x][y]
                    self.Crow2[x][y] = self.Crow2[_x][_y]
                    self.Crow2[_x][_y] = box
                print(self.Crow2)
            elif row == "3":
                if self.Crow1[x][y] == None and self.Crow1[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Crow3[x][y]
                    self.Crow3[x][y] = self.Crow3[_x][_y]
                    self.Crow3[_x][_y] = box
                print(self.Crow3)
            elif row == "4":
                if self.Crow4[x][y] == None and self.Crow4[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Crow4[x][y]
                    self.Crow4[x][y] = self.Crow4[_x][_y]
                    self.Crow4[_x][_y] = box
                print(self.Crow4)
            elif row == "5":
                if self.Crow5[x][y] == None and self.Crow5[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Crow5[x][y]
                    self.Crow5[x][y] = self.Crow5[_x][_y]
                    self.Crow5[_x][_y] = box
                print(sel5.Crow4)
        if kind == "D" and _kind == "D":
            if row == "1":
                if self.Drow1[x][y] == None and self.Drow1[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Drow1[x][y]
                    self.Drow1[x][y] = self.Drow1[_x][_y]
                    self.Drow1[_x][_y] = box
                    print(self.Drow1)
            elif row == "2":
                if self.Drow2[x][y] == None and self.Drow2[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Drow1[x][y]
                    self.Drow2[x][y] = self.Drow2[_x][_y]
                    self.Drow2[_x][_y] = box
                    print(self.Drow2)
            elif row == "3":
                if self.Drow1[x][y] == None and self.Drow1[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Drow3[x][y]
                    self.Drow3[x][y] = self.Drow3[_x][_y]
                    self.Drow3[_x][_y] = box
                    print(self.Drow3)
            elif row == "4":
                if self.Drow4[x][y] == None and self.Drow4[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Drow4[x][y]
                    self.Drow4[x][y] = self.Drow4[_x][_y]
                    self.Drow4[_x][_y] = box
                    print(self.Drow4)
            elif row == "5":
                if self.Drow5[x][y] == None and self.Drow5[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Drow5[x][y]
                    self.Drow5[x][y] = self.Drow5[_x][_y]
                    self.Drow5[_x][_y] = box
                    print(sel5.Drow4)
        if kind == "E" and _kind == "E":
            if row == "1":
                if self.Erow1[x][y] == None and self.Erow1[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Erow1[x][y]
                    self.Erow1[x][y] = self.Erow1[_x][_y]
                    self.Erow1[_x][_y] = box
                    print(self.Erow1)
            elif row == "2":
                if self.Erow2[x][y] == None and self.Erow2[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Erow1[x][y]
                    self.Erow2[x][y] = self.Erow2[_x][_y]
                    self.Erow2[_x][_y] = box
                    print(self.Erow2)
            elif row == "3":
                if self.Erow1[x][y] == None and self.Erow1[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Erow3[x][y]
                    self.Erow3[x][y] = self.Erow3[_x][_y]
                    self.Erow3[_x][_y] = box
                    print(self.Erow3)
            elif row == "4":
                if self.Erow4[x][y] == None and self.Erow4[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Erow4[x][y]
                    self.Erow4[x][y] = self.Erow4[_x][_y]
                    self.Erow4[_x][_y] = box
                print(self.Erow4)
            elif row == "5":
                if self.Erow5[x][y] == None and self.Erow5[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Erow5[x][y]
                    self.Erow5[x][y] = self.Erow5[_x][_y]
                    self.Erow5[_x][_y] = box
                print(sel5.Erow4)
            
                
                    
