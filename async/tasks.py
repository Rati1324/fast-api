x = [[2,3,4],
     [5,3,2],
     [5,3,5]]

no = True
for rowstart in range(0, len(x)-1):
    for rowend in range(0, len(x)-1):
        for colstart in range(0, len(x)-1):
            for colend in range(0, len(x)-1):
                for i in range(rowstart, len(x)-rowend):
                    for j in range(colstart, len(x)-colend):
                        if len(x)-colend - colstart != 1 and len(x)-rowend - rowstart != 1:
                            print(x[i][j], end='')
                            no = True
                    if no:
                        print()
                if no:
                    print("------")
                    no = False