def times_ten(start_index, end_index):
    dic={}
    for i in range(start_index, end_index+1):
        dic[i]=i*10
    return dic

def factorials(n):
    facs={}
    list=[]
    for i in range(1,n+1):
        y=1
        for x in range(1,i+1):
            b=x*y
            y=b
        facs[i]=y
    return facs
