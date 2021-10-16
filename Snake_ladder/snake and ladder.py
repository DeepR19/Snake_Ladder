b = input("> ").split(",")

ladder =0
snake = 0
for i in b:
    c = i.split(":")
  
    if(int(c[0]) < int(c[1])):
        ladder+=1
    else:
        snake +=1

print(snake, ladder)