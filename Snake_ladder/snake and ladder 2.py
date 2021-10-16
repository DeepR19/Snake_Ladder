st=0
board=[]

b = input("").split(",")
Dies = list( map( int, input("").split(",") ) )

for i in b:
    c = i.split(":")
    a = [int(c[0]) , int(c[1])]
    board.append(a)

data = dict(board)

for i in Dies:
    die = i
    st =st+ die

    for i in data:
        if(i == st):
            st = data.get(i)           
        else:
            st
    if(st>=100):
        break

if(st >= 100):
    print("Yes")
else:
    print("No")