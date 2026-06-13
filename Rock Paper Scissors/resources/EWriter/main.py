import time

class Writer():
    def asciiConverter(self,letter:str):
        _A = "  ██═██  \n ██   ██ \n█████████\n██     ██\n██     ██"
        _B = "███████  \n██    ██ \n███████  \n██    ██ \n███████  "
        _C = " ███████ \n██       \n██       \n██       \n ███████ "
        _D = "██████   \n██   ██  \n██    ██ \n██   ██  \n██████   "
        _E = "█████████\n██       \n███████  \n██       \n█████████"
        _K = "██    ██ \n██   ██  \n██████   \n██   ██  \n██    ██ "
        _M = "██     ██\n███   ███\n██ █ █ ██\n██  █  ██\n██     ██"
        _R = "███████  \n██    ██ \n███████  \n██   ██  \n██    ██ "
        _S = " ███████ \n██       \n ███████ \n       ██\n███████  "
        _T = "█████████\n   ██    \n   ██    \n   ██    \n   ██    "
        _I = "█████████\n   ██    \n   ██    \n   ██    \n█████████"
        _N = "██     ██\n███    ██\n██ █   ██\n██  █  ██\n██   ████"
        _G = " ███████ \n██       \n██  █████\n██     ██\n ███████ "
        _Y = "██     ██\n ██   ██ \n  █████  \n    ██   \n    ██   "
                
        table = {"A":_A,
                "B":_B,
                "C":_C,
                "D":_D,
                "E":_E,
                "G":_G,
                "I":_I,
                "K":_K,
                "M":_M,
                "N":_N,
                "R":_R,
                "S":_S,
                "T":_T,
                "Y":_Y,
                }
        
        return table[letter]   
    def convertList(self,asciiText:str):
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
    def write(self,text:str):
        lists = []
        for i in text:
            if i.isalpha():
                number = self.asciiConverter(i)
                number_list = self.convertList(number)
                lists.append(number_list)
            elif i == " ":
                lists.append(["    " for x in range(5)])

        for x in range(5):
            print()
            for i in lists:
                print(i[x] ,end = " ")
        print()
    def goodWriting(self,text:str,duration=0.05,end="\n"):
        for i in text:
            print(i,end="",flush=True)
            time.sleep(duration)
        print("",end=end)

    def goodDialogue(self,name,text:str,duration=0.05,end="\n"):
        print(f"{name} :",end="")
        self.goodWriting(text,duration,end=end)