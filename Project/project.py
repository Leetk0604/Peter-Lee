
def c1():
    c1={"",}
    c1.clear()
    direction=["E","W"]
    for boat in direction:
        for Moses in direction:
            for Pharaoh in direction:
                for Ahab in direction:
                    for Jezebel in direction:
                        for Servant1 in direction:
                            for Ananias in direction:
                                for Sapphira in direction:
                                    for Servant2 in direction:
                                        if Moses==Pharaoh and Moses==Ahab and Moses==Ananias and Moses!=boat:
                                            c1.add(boat+Moses+Pharaoh+Ahab+Jezebel+Servant1+Ananias+Sapphira+Servant2)

    return c1
def c2():
    c2={"",}
    c2.clear()
    direction=["E","W"]
    for boat in direction:
        for Moses in direction:
            for Pharaoh in direction:
                for Ahab in direction:
                    for Jezebel in direction:
                        for Servant1 in direction:
                            for Ananias in direction:
                                for Sapphira in direction:
                                    for Servant2 in direction:
                                        if Moses!=Pharaoh and (Pharaoh==Ahab or Pharaoh==Jezebel or Pharaoh==Servant1 or Pharaoh==Ananias or Pharaoh==Sapphira or Pharaoh==Servant2):
                                            c2.add(boat+Moses+Pharaoh+Ahab+Jezebel+Servant1+Ananias+Sapphira+Servant2)        
    
    return c2
def c3():
    c3={"",}
    c3.clear()
    direction=["E","W"]
    for boat in direction:
        for Moses in direction:
            for Pharaoh in direction:
                for Ahab in direction:
                    for Jezebel in direction:
                        for Servant1 in direction:
                            for Ananias in direction:
                                for Sapphira in direction:
                                    for Servant2 in direction:
                                        if (Ananias==Jezebel and Ahab!=Jezebel) or (Ananias==Servant1 and Ahab!=Servant1):
                                            c3.add(boat+Moses+Pharaoh+Ahab+Jezebel+Servant1+Ananias+Sapphira+Servant2)
    
    return c3
def c4():
    c4={''}
    c4.clear()
    direction=["E","W"]
    for boat in direction:
        for Moses in direction:
            for Pharaoh in direction:
                for Ahab in direction:
                    for Jezebel in direction:
                        for Servant1 in direction:
                            for Ananias in direction:
                                for Sapphira in direction:
                                    for Servant2 in direction:
                                        if (Ahab==Sapphira and Ananias!=Sapphira) or (Ahab==Servant2 and Ananias!=Servant2):
                                            c4.add(boat+Moses+Pharaoh+Ahab+Jezebel+Servant1+Ananias+Sapphira+Servant2)
    return c4
    
def violatec2c3():
    violatec2c3=c2().intersection(c3())
    return violatec2c3
def violatec2c4():
    violatec2c4=c2().intersection(c4())
    return violatec2c4
def violatec3c4():
    violatec3c4=c3().intersection(c4())
    return violatec3c4
def violatec2c3c4():
    violatec2c3c4=violatec2c3().intersection(c4())
    return violatec2c3c4
def onlyc2():
    onlyc2=c2().difference(violatec2c3())
    onlyc2=onlyc2.difference(violatec2c4())
    return onlyc2
def onlyc3():
    onlyc3=c3().difference(violatec2c3())
    onlyc3=onlyc3.difference(violatec3c4())
    return onlyc3
def onlyc4():
    onlyc4=c4().difference(violatec2c4())
    onlyc4=onlyc4.difference(violatec3c4())
    return onlyc4
def alllegalstate():
    state={"",}
    state.clear()
    direction=["E","W"]
    for boat in direction:
        for Moses in direction:
            for Pharaoh in direction:
                for Ahab in direction:
                    for Jezebel in direction:
                        for Servant1 in direction:
                            for Ananias in direction:
                                for Sapphira in direction:
                                    for Servant2 in direction:
                                        state.add(boat+Moses+Pharaoh+Ahab+Jezebel+Servant1+Ananias+Sapphira+Servant2)
    
    legalstate=state.difference(c1())
    legalstate=legalstate.difference(c2())
    legalstate=legalstate.difference(c3())
    legalstate=legalstate.difference(c4())
    legalstate=legalstate.difference(violatec2c3c4())
    register=[]
    for x in legalstate:
        register.append(x)
    register.sort()
    return register
usefulpath=set()
def solver():
    """
    The main program prints out a human-readable solution to the problem.
    # Input: None
    # Output: None
    """
    print("The set of legal states: (" , len(alllegalstate()),")")
    c=0                                                 #print the legal states 
    r=0
    for item in alllegalstate():
        if c==5:
            print(item)
            c=0
        else:
            print(item,end=' ')
            c=c+1
        r=r+1
    print()
    print("(C1): The set of illegal states that violates the constraint of having the boat with at least a man: (" , len(c1()),")")
    c=0                                                 #print the illegal states that violates the constraint of having the boat with at least a man(C1)
    r=0
    for item in c1():
        if c==5:
            print(item)
            c=0
        else:
            print(item,end=' ')
            c=c+1
        r=r+1
    print()
    print("(C2): The set of illegal states that violates the constraint of preventing Pharaoh from beating others:  (" , len(c2()),")")
    c=0                                                 #print the illegal states that violates the constraint of preventing Pharaoh from beating others(C2)
    r=0
    for item in c2():
        if c==5:
            print(item)
            c=0
        else:
            print(item,end=' ')
            c=c+1
        r=r+1
    print()
    print("(C3): The set of illegal states that violates the constraint of preventing Ananias from beating Ahab's household:  (" , len(c3()),")")

    c=0                                                 #print the illegal states that violates the constraint of preventing Ananias from beating Ahab's household(C3)
    r=0
    for item in c3():
        if c==5:
            print(item)
            c=0
        else:
            print(item,end=' ')
            c=c+1
        r=r+1
    print()            
    print("(C4): The set of illegal states that violates the constraint of preventing Ahab from beating Ananias's household: (" , len(c4()),")")
    c=0                                                 #print the illegal states that violates the constraint of preventing Ahab from beating Ananias's household(C4)
    r=0
    for item in c4():
        if c==5:
            print(item)
            c=0
        else:
            print(item,end=' ')
            c=c+1
        r=r+1
    print()
    print("The set of illegal states that violate both C2 and C3: (" , len(violatec2c3()),")")
    c=0                                                 #print the illegal states that violate both C2 and C3
    r=0
    for item in violatec2c3():
        if c==5:
            print(item)
            c=0
        else:
            print(item,end=' ')
            c=c+1
        r=r+1
    print()
    print("The set of illegal states that violate both C2 and C4: (" , len(violatec2c4()),")")
    c=0                                                 #print the illegal states that violate both C2 and C4
    r=0
    for item in violatec2c4():
        if c==5:
            print(item)
            c=0
        else:
            print(item,end=' ')
            c=c+1
        r=r+1
    print()
    print("The set of illegal states that violate both C3 and C4: (" , len(violatec3c4()),")")
    c=0                                                 #print the illegal states that violate both C3 and C4
    r=0
    for item in violatec3c4():
        if c==5:
            print(item)
            c=0
        else:
            print(item,end=' ')
            c=c+1
        r=r+1
    print()
    print("The set of illegal states that violate both C2 , C3 and C4: (" , len(violatec2c3c4()),")")
    c=0                                                 #print the illegal states that violate both C2 , C3 and C4
    r=0
    for item in violatec2c3c4():
        if c==5:
            print(item)
            c=0
        else:
            print(item,end=' ')
            c=c+1
        r=r+1
    print()
    print("The set of illegal states that violate only C2: (" , len(onlyc2()),")")
    c=0                                                 #print the illegal states that violate only C2
    r=0
    for item in onlyc2():
        if c==5:
            print(item)
            c=0
        else:
            print(item,end=' ')
            c=c+1
        r=r+1
    print()
    print("The set of illegal states that violate only C3: (" , len(onlyc3()),")")
    c=0                                                 #print the illegal states that violate only C
    r=0
    for item in onlyc3():
        if c==5:
            print(item)
            c=0
        else:
            print(item,end=' ')
            c=c+1
        r=r+1
    print()
    print("The set of illegal states that violate only C4: (" , len(onlyc4()),")")
    c=0                                                 #print the illegal states that violate only C4
    r=0
    for item in onlyc4():
        if c==5:
            print(item)
            c=0
        else:
            print(item,end=' ')
            c=c+1
        r=r+1
    print()
    print("SECTION B: FORMING A GRAPH")
    
    setAllStates = alllegalstate()                      # Generate a set of all possible states
                                                        # Each state consists of 9 characters, each of which could be
                                                        # E(ast)/W(est):
                                                        # 1st: Boat
                                                        # 2nd: Moses
                                                        # 3rd: Pharaoh
                                                        # 4th: Ahab (husband)
                                                        # 5th: Jezebel (wife)
                                                        # 6th: Ahab's servant
                                                        # 7th: Ananias (husband)
                                                        # 8th: Sapphira (wife)
                                                        # 9th: Ananias's servant

    G = genGraph(setAllStates)                          # Generate a graph G from the set of states (nodes)
    
    src = "EEEEEEEEE"                             
    des = "WWWWWWWWW"                  
    
    path = findShortestPath(G,src,des,path=[])
    print("There are ",len(usefulpath)," legal states that are part of at least one shortest path.")
    for item in sorted(usefulpath):                     #print the legal states that are part of at least one shortest path in sorted order
        register=[]
        for i in usefulpath:
            if i in G[item]:
                register.append(i)
        print(f"{item} {register}")
    print(f"There are {len(alllegalstate())-len(usefulpath)} legal states that are NOT part of any shortest path.")
    register=[]                                         #print the legal states that are Not part of any shortest path in sorted order
    c=0
    r=0
    for item in G:
        if item not in usefulpath:
            register.append(item)
    for item in register:
        if c==5:
            print(register[r])
            c=0
        else:
            print(register[r],end=' ')
            c=c+1
        r=r+1
    print()
    print("SECTION C: SHORTEST PATHS")
    print()
    printPath(path)
     

def genGraph(S):
     
    setLegalStates=[]
    
    graph={}
    for n in alllegalstate():
        setLegalStates.append(n)     
         
    for n in range(len(setLegalStates)):
        setNextNodes = nextStates(setLegalStates[n],setLegalStates)
        graph.update({setLegalStates[n]:setNextNodes})


    return graph



def nextStates(aState,allStates):
    """
    This function returns a set of states that a given state can go to.
    Input: A state (aState) and a set of a states (allStates)
    Output: A set of states from allStates that aState can go to (i.e., neighboring states
    """
    
    neighborStates = []
            
    # Determine which states could be reached by the given states
    for m in allStates:
        # A neighbor node if the two states differ by one or two elements
        # in their states
        if neighborNode(aState,m) == True:
            neighborStates.append(m)

    return neighborStates
def neighborNode(n1, n2):
    diff = 0
    if n1[0] != n2[0]:
        for i in range(1,9):
            if n1[i] == n1[0]:
                if n1[i] != n2[i] and (n1[1]!=n2[1] or n1[2]!=n2[2] or n1[3]!=n2[3] or n1[6]!=n2[6]):
                    diff = diff + 1
            else:
                if n1[i] != n2[i]:
                    return False
    else:
        return False
        
    if diff > 0 and diff < 3:
        return True
    else:
        return False

def findShortestPath(graph, start, end, path=[]):
    global usefulpath
    path = path + [start]
    if start == end:
        return path

    if not (start in graph):
        return None
    shortestPath = None
    for node in graph[start]:
        if node not in path:
            newpath = findShortestPath(graph, node, end, path)
            if newpath:
                if not shortestPath or len(newpath) < len(shortestPath):
                    shortestPath = newpath
                    for x in shortestPath:
                        usefulpath.add(x)

    return shortestPath


def printPath(path):


    East=["","Moses","Pharaoh","Ahab","Jezebel","servant of Ahab","Ananics","Sapphira","servant of Ananias"]
    West=["","","","","","","","",""]
    listPersons=["","Moses","Pharaoh","Ahab","Jezebel","servant of Ahab","Ananics","Sapphira","servant of Ananias"]
    for nodeOnPath in range(len(path)-1):
        East1=[]
        for item in East:
            if item != "":
                East1.append(item)
        West1=[]
        for item in West:
            if item != "":
                West1.append(item)
        
        print("East: ",sorted(East1))
        print("West: ",sorted(West1))        

        if path[nodeOnPath][0] == "E":
            fromDirection = "east"
            toDirection = "west"
        else:
            fromDirection = "west"
            toDirection = "east"

        whichPersonCrossing = ""

        for j in range(1,len(path[nodeOnPath])):
            if path[nodeOnPath][j] != path[nodeOnPath+1][j]:
                whichPersonCrossing = whichPersonCrossing + str(j)

        printLine = "The "
        if len(whichPersonCrossing) == 1:    
            printLine = printLine + listPersons[int(whichPersonCrossing[0])] + " goes"
        else:
            printLine = printLine + listPersons[int(whichPersonCrossing[0])] + " and " + listPersons[int(whichPersonCrossing[1])] + " go"
        for num in range (len(whichPersonCrossing)):
            if fromDirection == "east":
                East[int(whichPersonCrossing[num])]=""
            elif fromDirection == "west":
                West[int(whichPersonCrossing[num])]=""
            if toDirection =="east":
                East[int(whichPersonCrossing[num])]=listPersons[int(whichPersonCrossing[num])]
            elif toDirection == "west":
                West[int(whichPersonCrossing[num])]=listPersons[int(whichPersonCrossing[num])]

        printLine = printLine + " from the " + fromDirection + " to the " + toDirection + "."

        print("(",str(nodeOnPath+1),")",printLine)
        print()

solver()
