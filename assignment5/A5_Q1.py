def move(s1,s2):
    lists1=[]
    ship=0
    lists2=[]
    state=True
    #list[cabbage,goat,man,wolf]
    for letter in s1:
        if letter != " ":
            lists1.append(letter)
    for letter in s2:
        if letter != " ":
            lists2.append(letter)
    if lists1[0]==lists1[1] and lists1[2]!=lists1[1]:
        state=False
    if lists1[1]==lists1[3] and lists1[2]!=lists1[1]:
        state=False
    if lists2[0]==lists2[1] and lists2[2]!=lists2[1]:
        state=False
    if lists2[1]==lists2[3] and lists2[2]!=lists2[1]:
        state=False
    if lists1 == lists2:
        state =False
    if lists1[2] == lists2[2]:
        state =False
    for i in range (4):
        if lists1[i]!=lists2[i]:
            ship=ship+1
    if ship>2 :
        state = False
    return state
def statment(s1,s2):
    move = state
    lists11=[]
    lists22=[]
    direct=[]
    ship=[]
    txt=[]
    if  move== False :
        txt.append("Illegal move")
    else:
        for letter in s1:
            if letter != " ":
                lists11.append(letter)
        for letter in s2:
            if letter != " ":
                lists22.append(letter)
        if lists11[0] != lists22[0]:
            ship.append("Cabbage")
            if lists11[0] == "E":
                direct.append("East")
                direct.append("West")
            elif lists11[0] == "W":
                direct.append("West")
                direct.append("East")
        if lists11[1] != lists22[1]:
            ship.append("Goat")
            if lists11[1] == "E":
                direct.append("East")
                direct.append("West")
            elif lists11[1] == "W":
                direct.append("West")
                direct.append("East")
        if lists11[2] != lists22[2]:
            ship.append("Man")
            if lists11[2] == "E":
                direct.append("East")
                direct.append("West")
            elif lists11[2] == "W":
                direct.append("West")
                direct.append("East")
        if lists11[3] != lists22[3]:
            ship.append("Wolf")
            if lists11[3] == "E":
                direct.append("East")
                direct.append("West")
            elif lists11[3] == "W":
                direct.append("West")
                direct.append("East")
        txt.append(ship[0])
        if len(ship) ==2:
            txt.append("and")
            txt.append(ship[1])
        if len(ship) ==2:
            txt.append("move from")
        else:
            txt.append("moves from")
        txt.append(direct[0])
        txt.append("to")
        txt.append(direct[1])
    return txt
sol =("EEEE","EWWE","EWEE","WWWE","WEEE","WEWW","WEEW","WWWW")
for i in range(1,len(sol)):
    move(sol[i-1],sol[i])
    state=move(sol[i-1],sol[i])
    print(sol[i-1],sol[i],' '.join(map(str, statment(sol[i-1],sol[i]))))
sol =("EEEE","EWWE","EWEE","EWWE","EWEE","WWWE","WEEE","WEWW","WEEW","WWWW")
for i in range(1,len(sol)):
    move(sol[i-1],sol[i])
    state=move(sol[i-1],sol[i])
    print(sol[i-1],sol[i],' '.join(map(str, statment(sol[i-1],sol[i]))))
sol =("EEEE","EWWE","EWEE","WWWE","WWEE","WWWE","EWEE","WWWW")
for i in range(1,len(sol)):
    move(sol[i-1],sol[i])
    state=move(sol[i-1],sol[i])
    print(sol[i-1],sol[i],' '.join(map(str, statment(sol[i-1],sol[i]))))
