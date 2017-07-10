from WareHouse1 import WareHouse1
from WareHouse2 import WareHouse2
from WareHouse3 import WareHouse3
from WareHouse4 import WareHouse4
from WareHouse5 import WareHouse5
w1 = WareHouse1()
w2 = WareHouse2()
w3 = WareHouse3()
w4 = WareHouse4()
w5 = WareHouse5()

count = True
while count:
    input_id = raw_input("Product ID: ")
    item = input_id[1:5]
    kind = input_id[1]
    row = input_id[2]
    x = input_id[3]
    y = input_id[4]
    #warehouse 1
    if len(input_id) == 5 and input_id[1] == "A" or input_id[1] == "B" or input_id[1] == "C" or input_id[1] == "D" or input_id[1] == "E": 
        if input_id[0] == "0":
            w1.num0(row, int(x), int(y), kind)
        elif input_id[0] == "1":
            w1.num1(row, int(x), int(y), item, kind)
        elif input_id[0] == "2":
            w1.num2(row, kind)
        elif input_id[0] == "5":
            w1.num5(row, int(x), int(y), item, kind)
    #warehouse 2 
    elif len(input_id) == 5 and input_id[1] == "F" or input_id[1] == "G" or input_id[1] == "H" or input_id[1] == "I" or input_id[1] == "G": 
        if input_id[0] == "0":
            w2.num0(row, int(x), int(y), kind)
        elif input_id[0] == "1":
            w2.num1(row, int(x), int(y), item, kind)
        elif input_id[0] == "2":
            w2.num2(row, kind)
        elif input_id[0] == "5":
            w2.num5(row, int(x), int(y), item, kind)
    #warehouse 3
    elif len(input_id) == 5 and input_id[1] == "F" or input_id[1] == "G" or input_id[1] == "H" or input_id[1] == "I" or input_id[1] == "G": 
        if input_id[0] == "0":
            w3.num0(row, int(x), int(y), kind)
        elif input_id[0] == "1":
            w3.num1(row, int(x), int(y), item, kind)
        elif input_id[0] == "2":
            w3.num2(row, kind)
        elif input_id[0] == "5":
            w3.num5(row, int(x), int(y), item, kind)
    #warehouse 4
    elif len(input_id) == 5 and input_id[1] == "F" or input_id[1] == "G" or input_id[1] == "H" or input_id[1] == "I" or input_id[1] == "G": 
        if input_id[0] == "0":
            w4.num0(row, int(x), int(y), kind)
        elif input_id[0] == "1":
            w4.num1(row, int(x), int(y), item, kind)
        elif input_id[0] == "2":
            w4.num2(row, kind)
        elif input_id[0] == "5":
            w4.num5(row, int(x), int(y), item, kind)
    #warehouse 5
    elif len(input_id) == 5 and input_id[1] == "F" or input_id[1] == "G" or input_id[1] == "H" or input_id[1] == "I" or input_id[1] == "G": 
        if input_id[0] == "0":
            w4.num0(row, int(x), int(y), kind)
        elif input_id[0] == "1":
            w4.num1(row, int(x), int(y), item, kind)
        elif input_id[0] == "2":
            w4.num2(row, kind)
        elif input_id[0] == "5":
            w4.num5(row, int(x), int(y), item, kind)
    #command 30000, 40000, 9
    elif input_id == "30000": 
        w1.num3()
        w2.num3()
        w3.num3()
        w4.num3()
        w5.num3()
    elif input_id == "40000": 
        ware = raw_input("Ware House: ")
        if ware == "1": 
            w1.num4(ware)
        elif ware == "1":
            w2.num4(ware)
        elif ware == "1":
            w3.num4(ware)
        elif ware == "1":
            w4.num4(ware)
        elif ware == "1":
            w5.num4(ware)
    elif len(input_id) == 9 and input_id[0] == "9":
        _item = input_id[5:9]
        _kind = input_id[5]
        _row = input_id[6]
        _x = input_id[7]
        _y = input_id[8]
        if input_id[1] == "A" or input_id[1] == "B" or input_id[1] == "C" or input_id[1] == "D" or input_id[1] == "E" and input_id[1] == "A" or input_id[5] == "B" or input_id[5] == "C" or input_id[5] == "D" or input_id[5] == "E":
            w1.num9(row, int(x), int(y), kind, item, _row, int(_x), int(_y), _kind, _item)
        elif input_id[1] == "F" or input_id[1] == "G" or input_id[1] == "H" or input_id[1] == "I" or input_id[1] == "J" and input_id[1] == "F" or input_id[5] == "G" or input_id[5] == "H" or input_id[5] == "I" or input_id[5] == "J":
            w2.num9(row, int(x), int(y), kind, item, _row, int(_x), int(_y), _kind, _item)
        elif input_id[1] == "K" or input_id[1] == "L" or input_id[1] == "M" or input_id[1] == "N" or input_id[1] == "O" and input_id[1] == "K" or input_id[5] == "L" or input_id[5] == "M" or input_id[5] == "N" or input_id[5] == "O":
            w3.num9(row, int(x), int(y), kind, item, _row, int(_x), int(_y), _kind, _item)
        elif input_id[1] == "P" or input_id[1] == "Q" or input_id[1] == "R" or input_id[1] == "S" or input_id[1] == "T" and input_id[1] == "P" or input_id[5] == "Q" or input_id[5] == "R" or input_id[5] == "S" or input_id[5] == "T":
            w4.num9(row, int(x), int(y), kind, item, _row, int(_x), int(_y), _kind, _item)
        elif input_id[1] == "U" or input_id[1] == "V" or input_id[1] == "W" or input_id[1] == "X" or input_id[1] == "Y" and input_id[1] == "U" or input_id[5] == "V" or input_id[5] == "W" or input_id[5] == "X" or input_id[5] == "Y":
            w5.num9(row, int(x), int(y), kind, item, _row, int(_x), int(_y), _kind, _item)
        
    else:
        print("Command is ERROR!!!")
            
    ask = raw_input("Repeat Again \n 1.Yes \n 2.No \n ")
    if ask == "1":
        count = True
    elif ask == "2":
        count = False
