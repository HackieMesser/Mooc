def largest():

    with open("numbers.txt") as num:
        index=0
        for line in num:
            if index==0:
                larg=line
            elif larg<line:
                larg=line
            index+=1
            print(larg)
        return int(larg) 

def read_fruits():
    with open("fruits.csv") as file:
        dic={}
        for line in file:
            line=line.replace("\n","")
            line=line.split(";")
            name=line[0]
            price=line[1]
            price=float(price)

            dic[name]=price
           

        return dic

def matrix_sum():
    with open("matrix.txt") as text:
        sum=0

        for item in text:
            item=item.split(",")
        for items in item:
            sum+=int(items)
    return sum

matrix_sum()



#def matrix_max():
#def row_sums():


def matrix_sum():
    with open("matrix.txt") as text:
        sum=0

        for item in text:
            item=item.split(",")
            for items in item:
                items=items.replace("/n", "")
                sum+=int(items)
        #for items in item:
           # print(items)
            #sum+=int(items)
    return sum



def matrix_max():
    with open("matrix.txt") as maxy:
        largest="a"
        index=0
        for item in maxy:
            item=item.split(",")
            for items in item:
                items=int(items)
                if index==0:
                    largest = items
                else:
                    if items > largest:
                        largest=items
                index+=1
        return largest

def row_sums():
    with open("matrix.txt") as rsfile:
        listy=[]
        for line in rsfile:
            line=line.replace("/n", "")
            line=line.split(",")
            rowsum=0
            for item in line:
                #item=item.split(",")
                item=int(item)
                rowsum+=item
            listy.append(rowsum)
    return listy

