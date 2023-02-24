####tuples
#01
def create_tuple(x,y,z):
    c=x+y+z
    list=[x,y,z]
    list.sort()
    a=list[0]
    b=list[2]
    return (a,b,c)
#alt
def create_tuple(x,y,z):
    return (min([x,y,z]),max([x,y,z]),sum([x,y,z]))

#02
def oldest_person(people):
    index=0
    for i in people:
        if index==0:
            b=i[1]
        elif i[1]<b:
            b=i[1]
        index+=1
    for c in people:
        if c[1]==b:
            return c[0]
#03
def older_people(people, year):
    older=[]
    for i in people:
        if i[1]<year:
            older.append(i[0])
    return older
