def addTable():
    row=[]
    table=[]
    a=""
    for i in range(10) :
        row=[]
        for j in range(10):
            a=str(i+j)
            if i+j <10 :
                a="0"+a
            row.append(a)
        table.append(row)
    return table
            
def main():
    table = addTable()
    for item in table:
        print(item)
main()
