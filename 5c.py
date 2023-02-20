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

#phone book    
pbook={}
while True:
    cmd=input("command(1 search, 2 add, 3 quit)")
    if cmd =="1":
        search=input("name:")
        if search in pbook:
            print(pbook[search])
        else:
            print("no number")
    elif cmd =="2":
        name=input("name:")
        number=input("number:")
        pbook[name]=number
        print("ok!")
    elif cmd=="3":
        print("quitting...")
        break 
#phonebook2
        def main():
    pbook={}
    while True:
        cmd=input("command (1 search, 2 add, 3 quit): ")
        if cmd=="1":
            cmdfunc("1", pbook)
        elif cmd=="2":
            cmdfunc("2", pbook)
        else:
            break
    print("quitting...")
def cmdfunc(num, pbook):
    if num =="1":
        search=input("name: ")
        if search in pbook:
            for word in pbook[search]:
                print(word)
        else:
            print("no number")
    if num =="2":
        name=input("name: ")
        number = input("number: ")
        if name in pbook:
            pbook[name].append(number)
        else:
            pbook[name]=[number]
        print("ok!")
main()
