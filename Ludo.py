from random import random
set=0
max_turn=66
turn = 0
win=71
got1={}
got2={}
# again= 0
p1=0
p1s=0

p1_g1 = 0
p1_g2 = 0
p1_g3 = 0
p1_g4 = 0
p2_g1 = 0
p2_g2 = 0
p2_g3 = 0
p2_g4 = 0

goties = {
    "p1_g1": 0,
    "p1_g2": 0,
    "p1_g3": 0,
    "p1_g4": 0,

    "p2_g1": 0,
    "p2_g2": 0,
    "p2_g3": 0,
    "p2_g4": 0
}
game={
    1:0,
    2:0,
    3:0,
    4:0
}
p2=0
p2s=0
    
# player wants to play or exit
print("\n1: for play\n0: for Exit\n")
hu=1


def Wining(turn):   
         
    for i in range(4):
        uber= goties[f"p{turn+1}_g{i+1}"]

        if( uber > 71):
            print(f"Player_{turn+1} _{i+1}_ goti WIN")
            goties[f"p{turn+1}_g{i+1}"] = 7_2
            game[i+1]=1
        
        
            # print(f"Player_{turn+1} WIN")


def pg(ster,goti,die):
    val = 0
    dies ={
        "p1_g1":p1_g1,
        "p1_g2":p1_g2,
        "p1_g3":p1_g3,
        "p1_g4":p1_g4,
        "p2_g1":p2_g1,
        "p2_g2":p2_g2,
        "p2_g3":p2_g3,
        "p2_g4":p2_g4,
    }
    if(a==6):
        ster+=1

        if(ster>0):
            val = dies[goti]
            val+=die

            again = int(random()*6)+1
            print("DIE roll again",again)

            val += again
            if(again == 6):
                gain = int(random()*6)+1
                if(gain == 6):
                    print("Bad_Luck you got third 6")
                    val -= 12
                else:
                    print("DIE roll again again",gain)
                    val += gain

    if((ster>0) & (die<6)):
        val  += die 

    return (val,goti)
    

while(hu == 1 & hu != 0):
    turn = turn%2
    a = int(random()*6)+1
    
    print("___________________________________")
    
    # Check turn and set their number
    if(turn == 0):
        print("\t__First__Player__Turn__")
        if(a==6):
            p1s+=1
    else:
        print("\t__Second__Player__Turn__")
        if(a==6):
            p2s+=1
            

    # Enter Choice of players , what he want to do
    hu = int(input("Enter your choice : "))

    # which number come on die
    print("\t\tDIE Roll ",a,"\n")
    
    if(hu == 1):
    # Check turn of players
        if(turn == 0):
            if p1s>0:
                goti1 = int(input(">> Which GOTI to want to play : "))
                got1 =  pg(p1s, f"p{turn+1}_g{goti1}",a)
                
                goties[got1[1]] += got1[0]

                print(f"\t\tP1 score {goties['p1_g1']} {goties['p1_g2']} {goties['p1_g3']} {goties['p1_g4']}")
        else:
            if p2s>0:
                goti2 = int(input(">> Which GOTI to want to play : "))
                got2 =  pg(p2s, f"p{turn+1}_g{goti2}",a)

                goties[got2[1]] += got2[0]

                print(f"\t\tP1 score {goties['p2_g1']} {goties['p2_g2']} {goties['p2_g3']} {goties['p2_g4']}")

    # Goti Attack to other
        b = int(random()*6)+1
        
        for i in range(4):
            for j in range(4):
                first = goties[f"p1_g{i+1}"]
                second = goties[f"p2_g{j+1}"]

                if((first>0) & (second>0)):
                    if(first == second):
                        set=1
                        if(turn == 0):
                            goties[f"p2_g{j+1}"] = 0
                            print("You attack & DIE Roll ",b,"\n")
                            
                            confirm1 = int(input(">> Which GOTI to want to play : "))
                            
                            con1 =  pg(p2s, f"p{turn+1}_g{confirm1}", b)

                            goties[con1[1]] += con1[0]

                            print(f"\t\tP1 score {goties['p1_g1']} {goties['p1_g2']} {goties['p1_g3']} {goties['p1_g4']}")

                        else:
                            goties[f"p1_g{i+1}"]= 0
                            print("You attack & DIE Roll ",b,"\n")

                            confirm2 = int(input(">> Which GOTI to want to play : "))
                            
                            con2 =  pg(p2s, f"p{turn+1}_g{confirm2}", b)

                            goties[con2[1]] += con2[0]

                            print(f"\t\tP1 score {goties['p2_g1']} {goties['p2_g2']} {goties['p2_g3']} {goties['p2_g4']}")

                if(set==1):            
                    break


        
    # Wining Game acknowledgement
        if(turn==0):
            Wining(turn)
        else:
            Wining(turn)

    # Exit Code
    elif(hu ==0):
        if (turn==0):
            print("Player_1 EXIT 🏃‍♀️🏃‍♀️\n_____________\nPlayer_2 WIN!!🎊🎉\n")

            break
        else:
            print("Player_2 EXIT 🏃‍♀️🚴‍♂️\n_____________\nPlayer_1 WIN!!🎊🎉\n")
            break
    # For not valid Input
    else:
        print("Not Valid Number") 

    turn +=1
