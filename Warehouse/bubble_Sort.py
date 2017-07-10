def bubble_Sort(alist):
    while True:

        check = False
        try:

            for i in range(len(alist) + 1):
                for j in range(i):
                    if alist[i - 1][j] > alist[i - 1][j + 1]:
                        box = alist[i - 1][j]
                        alist[i - 1][j] = alist[i - 1][j + 1]
                        alist[i - 1][j + 1] = box
                        check = True
                    else:
                        pass
                        
        except IndexError:
            pass
        if check == False:
            break
           
    return alist


