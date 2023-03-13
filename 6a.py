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

#WIP
        text=text.split(",")
