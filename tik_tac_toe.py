array = [[0,0,0],
         [0,0,0],
         [0,0,0]]
# C=0
tik_tak_toe = [["C","C","C"],["C","C","C"],["C","C","C"]]
win=0
turn=0
def yup(r,c,d,index):
    setx=0
    sety=0
    setd1=0
    setd2=0
    if((array[0][2] & array[1][1]& array[2][0]) ==1):
        setd2 +=1

    for i in range(3):
        if(r == "r"):
            # print("r")
            if(array[index][i] == 1):
                setx+=1
        if(c == "c"):
            # print("c")
            if(array[i][index] == 1):
                sety+=1
        if(d == "d"):
            # print("d")
            if(array[i][i] == 1):
                setd1 +=1
        
    
    return setx,sety,setd1,setd2


    # print(a)


while True:
    
    if turn%2==0:
        print("\n\tFirst Player Turn ")
    else:
        print("\n\tSecond Player Turn ")

    r = list(map(int,input(">> Enter in format { row,column } ").split(",")))
    print()

    if array[r[0]][r[1]] == 1:
        print("\t   Already filled ")
    else:
        array[r[0]][r[1]] = 1
        turn+=1

    for i in range(3):
        print(tik_tak_toe[i])

  
    for i in range(3):
        a =yup("r","c","d",i)
        if((a[0]==3)|( a[1]==3)|( a[2]==3) | (a[3]==1)):
            win=1

    if win:print("WIN")


    print("\n_____________________________")

    
    
