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
#invert dictionary
def invert(dictionary:dict):
    new_dictionary ={}
    for key, value in dictionary.items():
        new_dictionary[value]=key
    dictionary.clear()
    for key,value in new_dictionary.items():
        dictionary[key]=value
#dic of numbers
def dict_of_numbers():
    numbers={}
    numbers[0]="zero"
    numbers[1]="one"
    numbers[11]="eleven"
    numbers[12]="twelve"
    numbers[13]="thirteen"
    numbers[14]="fourteen"
    numbers[15]="fifteen"
    numbers[18]="eighteen"
    listy=[16,17,19]

    i=0
    for tens in range(0,10):
        if tens == 0:
            tplace=""
        elif tens == 1:
            tplace="ten"
        elif tens == 2:
            tplace="twenty"
        elif tens == 3:
            tplace="thirty"
        elif tens == 4:
            tplace="forty"
        elif tens == 5:
            tplace="fifty"
        elif tens == 6:
            tplace="sixty"
        elif tens == 7:
            tplace="seventy"
        elif tens == 8:
            tplace="eighty"
        elif tens == 9:
            tplace="ninety"
        for ones in range(0,10):
            if ones == 0:
                oplace=""
            elif ones == 1:
                oplace="one"
            elif ones == 2:
                oplace="two"
            elif ones == 3:
                oplace="three"
            elif ones == 4:
                oplace="four"
            elif ones == 5:
                oplace="five"
            elif ones == 6:
                oplace="six"
            elif ones == 7:
                oplace="seven"
            elif ones == 8:
                oplace="eight"
            elif ones == 9:
                oplace="nine"
            if i not in numbers and i not in listy: 
                if ones>0 and tens>1:
                    numbers[i]=(f"{tplace}-{oplace}")
                else:
                    numbers[i]=(f"{tplace}{oplace}")
            elif i in listy:
                numbers[i]=(f"{oplace}teen")
            i+=1
    return numbers
if __name__== "__main__":
    numbers=dict_of_numbers()
    print(numbers[11])
    print(numbers[19])
    print(numbers[33])

    
#movies
def add_movie(database, name, director, year, runtime):
    movie=({"name":name, "director":director, "year":year, "runtime":runtime})
    database.append(movie)

if __name__ == '__main__':
    database = []
    add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
    add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
    print(database)

    
def find_movies(database, search_term):
    movies=[]
    for items in database:
        for dics in items:
            if search_term.lower() in dics["name"].lower():
                movies.append(dics)
    return movies

if __name__ == "__main__":
    database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
    {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
    {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}]

    my_movies = find_movies(database, "python")
    print(my_movies)


            
