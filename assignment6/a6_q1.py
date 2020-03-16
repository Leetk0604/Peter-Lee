def crypto(m,N,order):
    choice=input("Please enter your choice (E/D): ")
    while choice !="d" and choice!="D" and choice!="e" and choice!="E":
            choice=input("Invalid choice, please try again:")
    cache=[]    
    storage=""
    storagee=[]
    total=0
    a=0
    f=[]
    ordera=[]
    smalllist=""
    storageee=""
    
    if choice == "e" or choice == "E":
        for letter in m:
            if letter != " ":
                cache.append(letter)
                total=total+1
        while (total%N)!=0:
            cache.append("z")
            total=total+1
            if(total%N)==0:
                break
                
        listlength=int(total/N)
        
        for i in order:
            a=i-1
            for j in range(listlength):
                storage=storage+cache[a]
                a=a+N
        return storage
    elif choice == "D" or choice == "d":
        for letter in m:
            if letter != " ":
                cache.append(letter)
                total=total+1
        listlength=int(total/N)
        for i in range (listlength):
            b=i
            for j in range(N):
                smalllist=smalllist+cache[b]
                b=b+listlength
            storagee.append(smalllist)
            smalllist=""
        for i in storagee:
            f=[]
            ordera=[]
            for j in range (len(order)):
                ordera.append(order[j])
            for j in range (len(order)):
                f.append(i[j])
            for k in range (len (ordera)):
                for j in range (1,len(ordera)):
                    if  ordera[j]<ordera[j-1]:
                        c=f[j]
                        f[j]=f[j-1]
                        f[j-1]=c
                        c=ordera[j]
                        ordera[j]=ordera[j-1]
                        ordera[j-1]=c
            for z in f:
                storageee=storageee+z
        return storageee
print(crypto("hellohowdoyoudo",3,(1,2,3)))
# user inputs a b e in that order
print(crypto("hellohowdoyoudo",3,(2,3,1)))
# user inputs A b E in that order
print(crypto("eowydlhdoohloou",3,(2,3,1)))
# user inputs b C D in that order
print(crypto("ordpfhntanlntpoeeondtanayteimieaolrbffkz",4,
(2,3,1,4)))
# user inputs b D in that order
print(crypto("harrypotterandvoldemort",5,(2,1,4,3,5)))
# user inputs e
