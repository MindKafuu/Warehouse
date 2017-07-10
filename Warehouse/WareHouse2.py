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

class WareHouse2:
    def __init__(self):
        self.Frow1 = [[None] * 10 for i in range(10)]
        self.Frow2 = [[None] * 10 for i in range(10)]
        self.Frow3 = [[None] * 10 for i in range(10)]
        self.Frow4 = [[None] * 8 for i in range(8)]
        self.Frow5 = [[None] * 8 for i in range(8)]

        self.Grow1 = [[None] * 10 for i in range(10)]
        self.Grow2 = [[None] * 10 for i in range(10)]
        self.Grow3 = [[None] * 10 for i in range(10)]
        self.Grow4 = [[None] * 8 for i in range(8)]
        self.Grow5 = [[None] * 8 for i in range(8)]

        self.Hrow1 = [[None] * 10 for i in range(10)]
        self.Hrow2 = [[None] * 10 for i in range(10)]
        self.Hrow3 = [[None] * 10 for i in range(10)]
        self.Hrow4 = [[None] * 8 for i in range(8)]
        self.Hrow5 = [[None] * 8 for i in range(8)]

        self.Irow1 = [[None] * 10 for i in range(10)]
        self.Irow2 = [[None] * 10 for i in range(10)]
        self.Irow3 = [[None] * 10 for i in range(10)]
        self.Irow4 = [[None] * 8 for i in range(8)]
        self.Irow5 = [[None] * 8 for i in range(8)]

        self.Jrow1 = [[None] * 10 for i in range(10)]
        self.Jrow2 = [[None] * 10 for i in range(10)]
        self.Jrow3 = [[None] * 10 for i in range(10)]
        self.Jrow4 = [[None] * 8 for i in range(8)]
        self.Jrow5 = [[None] * 8 for i in range(8)]


    def num0(self, row, x, y, kind):
        if kind == "A":
            if row == "1":
                if belt.size < 10:
                    if self.Frow1[x][y] != None:
                        belt.add(Node(str(self.Frow1[x][y])))
                        self.Frow1[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Frow1)
            elif row == "2":
                if belt.size < 10:
                    if self.Frow2[x][y] != None:
                        belt.add(Node(str(self.Frow2[x][y])))
                        self.Frow2[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Frow2)
            elif row == "3":
                if belt.size < 10:
                    if self.Frow3[x][y] != None:
                        belt.add(Node(str(self.Frow3[x][y])))
                        self.Frow3[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Frow3)
            elif row == "4":
                if belt.size < 10:
                    if self.Frow4[x][y] != None:
                        belt.add(Node(str(self.Frow4[x][y])))
                        self.Frow4[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Frow4)
            elif row == "5":
                if belt.size < 10:
                    if self.Frow5[x][y] != None:
                        belt.add(Node(str(self.Frow5[x][y])))
                        self.Frow5[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Frow5)
        elif kind == "B":
            if row == "1":
                if belt.size < 10:
                    if self.Grow1[x][y] != None:
                        belt.add(Node(str(self.Grow1[x][y])))
                        self.Grow1[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Grow1)
            elif row == "2":
                if belt.size < 10:
                    if self.Grow2[x][y] != None:
                        belt.add(Node(str(self.Grow2[x][y])))
                        self.Grow2[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Grow2)
            elif row == "3":
                if belt.size < 10:
                    if self.Grow3[x][y] != None:
                        belt.add(Node(str(self.Grow3[x][y])))
                        self.Grow3[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Grow3)
            elif row == "4":
                if belt.size < 10:
                    if self.Grow4[x][y] != None:
                        belt.add(Node(str(self.Grow4[x][y])))
                        self.Grow4[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Grow4)
            elif row == "5":
                if belt.size < 10:
                    if self.Grow5[x][y] != None:
                        belt.add(Node(str(self.Grow5[x][y])))
                        self.Grow5[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Grow5)
        elif kind == "C":
            if row == "1":
                if belt.size < 10:
                    if self.Hrow1[x][y] != None:
                        belt.add(Node(str(self.Hrow1[x][y])))
                        self.Hrow1[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Hrow1)
            elif row == "2":
                if belt.size < 10:
                    if self.Hrow2[x][y] != None:
                        belt.add(Node(str(self.Hrow2[x][y])))
                        self.Hrow2[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Hrow2)
            elif row == "3":
                if belt.size < 10:
                    if self.Hrow3[x][y] != None:
                        belt.add(Node(str(self.Hrow3[x][y])))
                        self.Hrow3[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Hrow3)
            elif row == "4":
                if belt.size < 10:
                    if self.Hrow4[x][y] != None:
                        belt.add(Node(str(self.Hrow4[x][y])))
                        self.Hrow4[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Hrow4)
            elif row == "5":
                if belt.size < 10:
                    if self.Hrow5[x][y] != None:
                        belt.add(Node(str(self.Hrow5[x][y])))
                        self.Hrow5[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Hrow5)
        elif kind == "D":
            if row == "1":
                if belt.size < 10:
                    if self.Irow1[x][y] != None:
                        belt.add(Node(str(self.Irow1[x][y])))
                        self.Irow1[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Irow1)
            elif row == "2":
                if belt.size < 10:
                    if self.Irow2[x][y] != None:
                        belt.add(Node(str(self.Irow2[x][y])))
                        self.Irow2[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Irow2)
            elif row == "3":
                if belt.size < 10:
                    if self.Irow3[x][y] != None:
                        belt.add(Node(str(selfD.row3[x][y])))
                        self.Irow3[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Irow3)
            elif row == "4":
                if belt.size < 10:
                    if self.Irow4[x][y] != None:
                        belt.add(Node(str(self.Irow4[x][y])))
                        self.Irow4[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Irow4)
            elif row == "5":
                if belt.size < 10:
                    if self.Irow5[x][y] != None:
                        belt.add(Node(str(self.Irow5[x][y])))
                        self.Irow5[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Irow5)
        elif kind == "E":
            if row == "1":
                if belt.size < 10:
                    if self.Jrow1[x][y] != None:
                        belt.add(Node(str(self.Jrow1[x][y])))
                        self.Jrow1[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Jrow1)
            elif row == "2":
                if belt.size < 10:
                    if self.Jrow2[x][y] != None:
                        belt.add(Node(str(self.Jrow2[x][y])))
                        self.Jrow2[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Jrow2)
            elif row == "3":
                if belt.size < 10:
                    if self.Jrow3[x][y] != None:
                        belt.add(Node(str(self.Jrow3[x][y])))
                        self.Jrow3[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Jrow3)
            elif row == "4":
                if belt.size < 10:
                    if self.Jrow4[x][y] != None:
                        belt.add(Node(str(self.Jrow4[x][y])))
                        self.Jrow4[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Jrow4)
            elif row == "5":
                if belt.size < 10:
                    if self.Jrow5[x][y] != None:
                        belt.add(Node(str(self.Jrow5[x][y])))
                        self.Jrow5[x][y] = None
                    else:
                        print("Slot is empty. Cannot retrieve the product.")
                else:
                    print("Belt is full. Cannot retrieve the product")
                print("Belt = " + str(belt))
                print("Size of Belt = " + str(belt.size))
                print(self.Jrow5)

    def num1(self, row, x, y, item, kind):
        if kind == "A":
            if row == "1":
                if self.Frow1[x][y] == None:
                    self.Frow1[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Frow1)
            elif row == "2":
                if self.Frow2[x][y] == None:
                    self.Frow2[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Frow2)
            elif row == "3":
                if self.Frow3[x][y] == None:
                    self.Frow3[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Frow3)
            elif row == "4":
                if self.Frow4[x][y] == None:
                    self.Frow4[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Frow4)
            elif row == "5":
                if self.Frow5[x][y] == None:
                    self.Frow5[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Frow5)
        elif kind == "B":
            if row == "1":
                if self.Grow1[x][y] == None:
                    self.Grow1[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Grow1)
            elif row == "2":
                if self.Grow2[x][y] == None:
                    self.Grow2[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Grow2)
            elif row == "3":
                if self.Grow3[x][y] == None:
                    self.Grow3[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Grow3)
            elif row == "4":
                if self.Grow4[x][y] == None:
                    self.Grow4[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Grow4)
            elif row == "5":
                if self.Grow5[x][y] == None:
                    self.Grow5[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Grow5)
        elif kind == "C":
            if row == "1":
                if self.Hrow1[x][y] == None:
                    self.Hrow1[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Hrow1)
            elif row == "2":
                if self.Hrow2[x][y] == None:
                    self.Hrow2[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Hrow2)
            elif row == "3":
                if self.Hrow3[x][y] == None:
                    self.Hrow3[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Hrow3)
            elif row == "4":
                if self.Hrow4[x][y] == None:
                    self.Hrow4[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Hrow4)
            elif row == "5":
                if self.Hrow5[x][y] == None:
                    self.Hrow5[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Hrow5)
        elif kind == "D":
            if row == "1":
                if self.Irow1[x][y] == None:
                    self.Irow1[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Irow1)
            elif row == "2":
                if self.Irow2[x][y] == None:
                    self.Irow2[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Irow2)
            elif row == "3":
                if self.Irow3[x][y] == None:
                    self.Irow3[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Irow3)
            elif row == "4":
                if self.Irow4[x][y] == None:
                    self.Irow4[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Irow4)
            elif row == "5":
                if self.Irow5[x][y] == None:
                    self.Irow5[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Irow5)
        elif kind == "E":
            if row == "1":
                if self.Jrow1[x][y] == None:
                    self.Jrow1[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Jrow1)
            elif row == "2":
                if self.Jrow2[x][y] == None:
                    self.Jrow2[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Jrow2)
            elif row == "3":
                if self.Jrow3[x][y] == None:
                    self.Jrow3[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Jrow3)
            elif row == "4":
                if self.Jrow4[x][y] == None:
                    self.Jrow4[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Jrow4)
            elif row == "5":
                if self.Jrow5[x][y] == None:
                    self.Jrow5[x][y] = item
                    print("Storing Successfully!")
                else:
                    print("Slot is occupied. Cannot store the product.")
                print(self.Jrow5)

    def num2(self, row, kind): 
        if kind == "A":
            if row == "1":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Frow1))
            elif row == "2":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Frow2))
            elif row == "3":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Frow3))
            elif row == "4":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Frow4))
            elif row == "5":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Frow5))
        elif kind == "B":
            if row == "1":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Grow1))
            elif row == "2":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Grow2))
            elif row == "3":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Grow3))
            elif row == "4":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Grow4))
            elif row == "5":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Grow5))
        elif kind == "C":
            if row == "1":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Hrow1))
            elif row == "2":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Hrow2))
            elif row == "3":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Hrow3))
            elif row == "4":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Hrow4))
            elif row == "5":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Hrow5))
        elif kind == "D":
            if row == "1":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Irow1))
            elif row == "2":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Irow2))
            elif row == "3":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Irow3))
            elif row == "4":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Irow4))
            elif row == "5":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Irow5))
        elif kind == "E":
            if row == "1":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Jrow1))
            elif row == "2":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Jrow2))
            elif row == "3":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Jrow3))
            elif row == "4":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Jrow4))
            elif row == "5":
                print("Sorting process for warehouse 1 is complete.")
                print(bubble_Sort(self.Jrow5))

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
        for i in self.Frow1:
            for j in i:
                if j != None:
                    count1 = count1 + 1
                    s1 = s1 + j + ", "
                else:
                    pass
        for i in self.Frow2:
            for j in i:
                if j != None:
                    count2 = count2 + 1
                    s2 = s2 + j + ", "
                else:
                    pass
        for i in self.Frow3:
            for j in i:
                if j != None:
                    count3 = count3 + 1
                    s3 = s3 + j + ", "
                else:
                    pass
        for i in self.Frow4:
            for j in i:
                if j != None:
                    count4 = count4 + 1
                    s4 = s4 + j + ", "
                else:
                    pass
        for i in self.Frow5:
            for j in i:
                if j != None:
                    count5 = count5 + 1
                    s5 = s5 + j + ", "
                else:
                    pass
        for i in self.Grow1:
            for j in i:
                if j != None:
                    count1 = count1 + 1
                    s1 = s1 + j + ", "
                else:
                    pass
        for i in self.Grow2:
            for j in i:
                if j != None:
                    count2 = count2 + 1
                    s2 = s2 + j + ", "
                else:
                    pass
        for i in self.Grow3:
            for j in i:
                if j != None:
                    count3 = count3 + 1
                    s3 = s3 + j + ", "
                else:
                    pass
        for i in self.Grow4:
            for j in i:
                if j != None:
                    count4 = count4 + 1
                    s4 = s4 + j + ", "
                else:
                    pass
        for i in self.Grow5:
            for j in i:
                if j != None:
                    count5 = count5 + 1
                    s5 = s5 + j + ", "
                else:
                    pass
        for i in self.Hrow1:
            for j in i:
                if j != None:
                    count1 = count1 + 1
                    s1 = s1 + j + ", "
                else:
                    pass
        for i in self.Hrow2:
            for j in i:
                if j != None:
                    count2 = count2 + 1
                    s2 = s2 + j + ", "
                else:
                    pass
        for i in self.Hrow3:
            for j in i:
                if j != None:
                    count3 = count3 + 1
                    s3 = s3 + j + ", "
                else:
                    pass
        for i in self.Hrow4:
            for j in i:
                if j != None:
                    count4 = count4 + 1
                    s4 = s4 + j + ", "
                else:
                    pass
        for i in self.Hrow5:
            for j in i:
                if j != None:
                    count5 = count5 + 1
                    s5 = s5 + j + ", "
                else:
                    pass
        for i in self.Irow1:
            for j in i:
                if j != None:
                    count1 = count1 + 1
                    s1 = s1 + j + ", "
                else:
                    pass
        for i in self.Irow2:
            for j in i:
                if j != None:
                    count2 = count2 + 1
                    s2 = s2 + j + ", "
                else:
                    pass
        for i in self.Irow3:
            for j in i:
                if j != None:
                    count3 = count3 + 1
                    s3 = s3 + j + ", "
                else:
                    pass
        for i in self.Irow4:
            for j in i:
                if j != None:
                    count4 = count4 + 1
                    s4 = s4 + j + ", "
                else:
                    pass
        for i in self.Irow5:
            for j in i:
                if j != None:
                    count5 = count5 + 1
                    s5 = s5 + j + ", "
                else:
                    pass
        for i in self.Jrow1:
            for j in i:
                if j != None:
                    count1 = count1 + 1
                    s1 = s1 + j + ", "
                else:
                    pass
        for i in self.Jrow2:
            for j in i:
                if j != None:
                    count2 = count2 + 1
                    s2 = s2 + j + ", "
                else:
                    pass
        for i in self.Jrow3:
            for j in i:
                if j != None:
                    count3 = count3 + 1
                    s3 = s3 + j + ", "
                else:
                    pass
        for i in self.Jrow4:
            for j in i:
                if j != None:
                    count4 = count4 + 1
                    s4 = s4 + j + ", "
                else:
                    pass
        for i in self.Jrow5:
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
                if self.Frow1[x][y] != None:
                    if item == self.Frow1[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
            elif row == "2":
                if self.Frow2[x][y] != None:
                    if item == self.Frow2[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
            elif row == "3":
                if self.Frow3[x][y] != None:
                    if item == self.Frow3[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
            elif row == "4":
                if self.Frow4[x][y] != None:
                    if item == self.Frow4[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
            elif row == "5":
                if self.Frow5[x][y] != None:
                    if item == self.Frow5[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
        if kind == "B":
            if row == "1":
                if self.Grow1[x][y] != None:
                    if item == self.Grow1[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
            elif row == "2":
                if self.Grow2[x][y] != None:
                    if item == self.Grow2[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
            elif row == "3":
                if self.Grow3[x][y] != None:
                    if item == self.Grow3[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
            elif row == "4":
                if self.Grow4[x][y] != None:
                    if item == self.Grow4[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
            elif row == "5":
                if self.Grow5[x][y] != None:
                    if item == self.Grow5[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
        if kind == "C":
            if row == "1":
                if self.Hrow1[x][y] != None:
                    if item == self.Hrow1[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
            elif row == "2":
                if self.Hrow2[x][y] != None:
                    if item == self.Hrow2[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
            elif row == "3":
                if self.Hrow3[x][y] != None:
                    if item == self.Hrow3[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
            elif row == "4":
                if self.Hrow4[x][y] != None:
                    if item == self.Hrow4[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
            elif row == "5":
                if self.Hrow5[x][y] != None:
                    if item == self.Hrow5[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
        if kind == "D":
            if row == "1":
                if self.Irow1[x][y] != None:
                    if item == self.Irow1[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
            elif row == "2":
                if self.Irow2[x][y] != None:
                    if item == self.Irow2[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
            elif row == "3":
                if self.Irow3[x][y] != None:
                    if item == self.Irow3[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
            elif row == "4":
                if self.Irow4[x][y] != None:
                    if item == self.Irow4[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
            elif row == "5":
                if self.Irow5[x][y] != None:
                    if item == self.Irow5[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
        if kind == "E":
            if row == "1":
                if self.Jrow1[x][y] != None:
                    if item == self.Jrow1[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
            elif row == "2":
                if self.Jrow2[x][y] != None:
                    if item == self.Jrow2[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
            elif row == "3":
                if self.Jrow3[x][y] != None:
                    if item == self.Jrow3[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
            elif row == "4":
                if self.Jrow4[x][y] != None:
                    if item == self.Jrow4[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")
            elif row == "5":
                if self.Jrow5[x][y] != None:
                    if item == self.Jrow5[x][y]:
                        print("Found the product at " + item)
                else:
                    print("Product not found.")

    def num9(self, row, x, y, kind, item, _row, _x, _y, _kind, _item):
        if kind == "A" and _kind == "A":
            if row == "1":
                if self.Frow1[x][y] == None and self.Frow1[_x][_y] == None:
                     print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Frow1[x][y]
                    self.Frow1[x][y] = self.Frow1[_x][_y]
                    self.Frow1[_x][_y] = box
                print(self.Frow1)
            elif row == "2":
                if self.Frow2[x][y] == None and self.Frow2[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Frow1[x][y]
                    self.Frow2[x][y] = self.Frow2[_x][_y]
                    self.Frow2[_x][_y] = box
                print(self.Frow2)
            elif row == "3":
                if self.Frow1[x][y] == None and self.Frow1[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Frow3[x][y]
                    self.Frow3[x][y] = self.Frow3[_x][_y]
                    self.Frow3[_x][_y] = box
                print(self.Frow3)
            elif row == "4":
                if self.Frow4[x][y] == None and self.Frow4[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Frow4[x][y]
                    self.Frow4[x][y] = self.Frow4[_x][_y]
                    self.Frow4[_x][_y] = box
                print(self.Frow4)
            elif row == "5":
                if self.Frow5[x][y] == None and self.Frow5[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Frow5[x][y]
                    self.Frow5[x][y] = self.Frow5[_x][_y]
                    self.Frow5[_x][_y] = box
                    print(sel5.Arow4)
        if kind == "B" and _kind == "B":
            if row == "1":
                if self.Grow1[x][y] == None and self.Grow1[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Grow1[x][y]
                    self.Grow1[x][y] = self.Grow1[_x][_y]
                    self.Grow1[_x][_y] = box
                print(self.Grow1)
            elif row == "2":
                if self.Grow2[x][y] == None and self.Grow2[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Grow1[x][y]
                    self.Grow2[x][y] = self.Grow2[_x][_y]
                    self.Grow2[_x][_y] = box
                print(self.Grow2)
            elif row == "3":
                if self.Grow1[x][y] == None and self.Grow1[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Grow3[x][y]
                    self.Grow3[x][y] = self.Grow3[_x][_y]
                    self.Grow3[_x][_y] = box
                print(self.Grow3)
            elif row == "4":
                if self.Grow4[x][y] == None and self.Grow4[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Grow4[x][y]
                    self.Grow4[x][y] = self.Grow4[_x][_y]
                    self.Grow4[_x][_y] = box
                print(self.Grow4)
            elif row == "5":
                if self.Grow5[x][y] == None and self.Grow5[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Grow5[x][y]
                    self.Grow5[x][y] = self.Grow5[_x][_y]
                    self.Grow5[_x][_y] = box
                    print(sel5.Brow4)
        if kind == "C" and _kind == "C":
            if row == "1":
                if self.Hrow1[x][y] == None and self.Hrow1[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Hrow1[x][y]
                    self.Hrow1[x][y] = self.Hrow1[_x][_y]
                    self.Hrow1[_x][_y] = box
                print(self.Hrow1)
            elif row == "2":
                if self.Hrow2[x][y] == None and self.Hrow2[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Hrow1[x][y]
                    self.Hrow2[x][y] = self.Hrow2[_x][_y]
                    self.Hrow2[_x][_y] = box
                print(self.Hrow2)
            elif row == "3":
                if self.Hrow1[x][y] == None and self.Hrow1[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Hrow3[x][y]
                    self.Hrow3[x][y] = self.Hrow3[_x][_y]
                    self.Hrow3[_x][_y] = box
                print(self.Hrow3)
            elif row == "4":
                if self.Hrow4[x][y] == None and self.Hrow4[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Hrow4[x][y]
                    self.Hrow4[x][y] = self.Hrow4[_x][_y]
                    self.Hrow4[_x][_y] = box
                print(self.Hrow4)
            elif row == "5":
                if self.Hrow5[x][y] == None and self.Hrow5[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Hrow5[x][y]
                    self.Hrow5[x][y] = self.Hrow5[_x][_y]
                    self.Hrow5[_x][_y] = box
                print(sel5.Crow4)
        if kind == "D" and _kind == "D":
            if row == "1":
                if self.Irow1[x][y] == None and self.Irow1[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Irow1[x][y]
                    self.Irow1[x][y] = self.Irow1[_x][_y]
                    self.Irow1[_x][_y] = box
                    print(self.Irow1)
            elif row == "2":
                if self.Irow2[x][y] == None and self.Irow2[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Irow1[x][y]
                    self.Irow2[x][y] = self.Irow2[_x][_y]
                    self.Irow2[_x][_y] = box
                    print(self.Irow2)
            elif row == "3":
                if self.Irow1[x][y] == None and self.Irow1[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Irow3[x][y]
                    self.Irow3[x][y] = self.Irow3[_x][_y]
                    self.Irow3[_x][_y] = box
                    print(self.Irow3)
            elif row == "4":
                if self.Irow4[x][y] == None and self.Irow4[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Irow4[x][y]
                    self.Irow4[x][y] = self.Irow4[_x][_y]
                    self.Irow4[_x][_y] = box
                    print(self.Irow4)
            elif row == "5":
                if self.Irow5[x][y] == None and self.Irow5[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Irow5[x][y]
                    self.Irow5[x][y] = self.Irow5[_x][_y]
                    self.Irow5[_x][_y] = box
                    print(sel5.Drow4)
        if kind == "E" and _kind == "E":
            if row == "1":
                if self.Jrow1[x][y] == None and self.Jrow1[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Jrow1[x][y]
                    self.Jrow1[x][y] = self.Jrow1[_x][_y]
                    self.Jrow1[_x][_y] = box
                    print(self.Jrow1)
            elif row == "2":
                if self.Jrow2[x][y] == None and self.Jrow2[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Jrow1[x][y]
                    self.Jrow2[x][y] = self.Jrow2[_x][_y]
                    self.Jrow2[_x][_y] = box
                    print(self.Jrow2)
            elif row == "3":
                if self.Jrow1[x][y] == None and self.Jrow1[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Jrow3[x][y]
                    self.Jrow3[x][y] = self.Jrow3[_x][_y]
                    self.Jrow3[_x][_y] = box
                    print(self.Jrow3)
            elif row == "4":
                if self.Jrow4[x][y] == None and self.Jrow4[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Jrow4[x][y]
                    self.Jrow4[x][y] = self.Jrow4[_x][_y]
                    self.Jrow4[_x][_y] = box
                print(self.Jrow4)
            elif row == "5":
                if self.Jrow5[x][y] == None and self.Jrow5[_x][_y] == None:
                    print("Slot is occupied. Failed to move.")
                else:
                    print("Move product " + item + " to " + _item)
                    box = self.Jrow5[x][y]
                    self.Jrow5[x][y] = self.Jrow5[_x][_y]
                    self.Jrow5[_x][_y] = box
                print(sel5.Erow4)
            
                
                    
