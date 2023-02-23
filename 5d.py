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
