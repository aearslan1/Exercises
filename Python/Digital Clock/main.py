from datetime import datetime
import os
import time
def asciiConverter(number:int):   
    _0 = "  ___   \n / _ \\  \n| | | | \n| | | | \n| |_| | \n \\___/  "
    _1 = "  __    \n /_ |   \n  | |   \n  | |   \n  | |   \n  |_|   "
    _2 = " ___    \n|__ \\   \n   ) |  \n  / /   \n / /_   \n|____|  "
    _3 = " ____   \n|___ \\  \n  __) | \n |__ <  \n ___) | \n|____/  "
    _4 = " _  _   \n| || |  \n| || |_ \n|__   _|\n   | |  \n   |_|  "
    _5 = " _____  \n| ____| \n| |__   \n|___ \\  \n ____) |\n|_____/ "
    _6 = "  __    \n / /    \n/ /_    \n| '_ \\  \n| (_) | \n \\___/  "
    _7 = " ______ \n|____  |\n    / / \n   / /  \n  / /   \n /_/    "
    _8 = "  ___   \n / _ \\  \n| (_) | \n > _ <  \n| (_) | \n \\___/  "
    _9 = "  ___   \n / _ \\  \n| (_) | \n \\__, | \n   / /  \n  /_/   "

    table = {0:_0,1:_1,2:_2,3:_3,4:_4,5:_5,6:_6,7:_7,8:_8,9:_9}

    return table[number]
    
def convertList(asciiText:str):
    pack = ""
    _list = []
    for indeks,i in enumerate(asciiText):  
        if i != "\n":
            pack += i
        if i == "\n" or indeks  + 1== len(asciiText):
            _list.append(pack)
            pack = ""
            continue
        
    return _list

def artPrinter(text:str):
    lists = []
    for i in text:
        if i.isdigit():
            number = asciiConverter(int(i))
            number_list = convertList(number)
            lists.append(number_list)
        elif i == " ":
            lists.append(["    " for x in range(6)])
        
        elif i == ":":
            _colon = "         \n    _    \n   (_)   \n    _    \n   (_)   \n         "
            list_of_colon = convertList(_colon)
            lists.append(list_of_colon)
    
    for x in range(6):
        print()
        for i in lists:
            print(i[x] ,end = " ")
    print()
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
while True:
    clear()
    now = datetime.now()
    artPrinter(now.strftime("%H:%M:%S"))
    time.sleep(1)
    
    
