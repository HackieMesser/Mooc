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


#wip
def read_fruits():
    with open("fruits.csv") as file:
        for line in file:
            file.split(";")
