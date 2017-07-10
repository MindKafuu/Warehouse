def bubbleSort(alist):
    while True:
        check = False
        try:     
            for i in range(len(alist)):
                if alist[i] > alist[i + 1]:
                    box = alist[i]
                    alist[i] = alist[i + 1]
                    alist[i + 1] = box
                    check = True
                else:
                    pass
                        
        except IndexError:
            pass
        if check == False:
            break
        
    return alist

