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
#histogram
def histogram(string:str):
    dic={}
    for i in string:
        if i not in dic:
            dic[i]=0
        dic[i]+=1
    for y, v in dic.items():
        stars=v*"*"
        print(f"{y} {stars}")
if __name__ == "__main__":
    string = "abba"
    histogram(string)
