from resources.EWriter.main import Writer
import os
import time
import sys
import random

EWriter = Writer()
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
def asciiConverter(number:int):   

    _1 = "      _______      \n---'   ____)____   \n      (_________)  \n      (_________)  \n      (________)   \n---.__(_____)      "

    _2 = "    ___________    \n---'   ________)___\n          ________)\n          ________)\n       ___________)\n---.____________)  "

    _3 = "    _______        \n---'   ____)____   \n          ______)  \n       __________)\n      (____)       \n---.__(___)        "
    
    _4 = "      _______      \n   ____(____   '---\n  (_________)      \n  (_________)      \n   (________)      \n      (_____)__.---"

    _5 = "    ___________    \n___(________   '---\n(________          \n(________          \n(___________       \n  (____________.---"

    _6 = "        _______    \n   ____(____   '---\n  (______          \n (__________       \n       (____)      \n        (___)__.---"
    table = {1:_1,
             2:_2,
             3:_3,
             4:_4,
             5:_5,
             6:_6}

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

class Game():
    def __init__(self):
        self.player_name = ""
        self.playerScore = 0
        self.computerScore = 0
    def whoWin(self,player:int,com:int):
        if (player == 1 and com == 4) or (player == 2 and com == 5) or (player == 3 and com == 6):
            return "\033[1;33mBERABERE\033[0m"
        elif (player == 1 and com == 6) or (player == 2 and com == 4) or (player == 3 and com == 5):
            return f"\033[1;32m{self.player_name} KAZANDI!\033[0m"
        
        else:
            return "\033[1;31mCOMPUTER KAZANDI!\033[0m"
        
    def resultScreen(self,playerStatue:int,computerStatue:int,spaceAmount=20):
        if self.whoWin(playerStatue,computerStatue) == f"\033[1;32m{self.player_name} KAZANDI!\033[0m":
            self.playerScore += 1
        elif self.whoWin(playerStatue,computerStatue) == "\033[1;31mCOMPUTER KAZANDI!\033[0m":
            self.computerScore += 1
        print(f"{" "*spaceAmount}{self.player_name.upper()}({self.playerScore}){" "*spaceAmount}   -{" "*spaceAmount}COMPUTER({self.computerScore}){" "*spaceAmount}")
        print(f"{((4*spaceAmount)+len(self.player_name)+9)*"_"}")
        artPrinter(f"{" "*(spaceAmount//6)}{playerStatue}{" "*(spaceAmount//8)}:{" "*(spaceAmount//8)}{computerStatue}")
        print(f"{" "*(spaceAmount+2)}{self.converter(playerStatue)}{" "*(2*spaceAmount+8)}{self.converter(computerStatue)}")
        resultSpace = (((4*spaceAmount)+len(self.player_name)+9 - len(self.whoWin(playerStatue,computerStatue))) // 2) + 8
        print(f"{" "*resultSpace}{self.whoWin(playerStatue,computerStatue)}{" "*resultSpace}")
        print(f"{((4*spaceAmount)+len(self.player_name)+9)*"_"}")
        
    def converter(self,number:int):
        convert_map = {
            1:"Taş",
            2:"Kağıt",
            3:"Makas",
            4:"Taş",
            5:"Kağıt",
            6:"Makas"
        }
        return convert_map[number]

    def mainMenu(self):
        clear()
        print("_"*90)
        EWriter.write("TAS KAGIT")
        EWriter.write("   MAKAS")
        print("\n")
        a = input(f"{" "*23}\033[1;30m(Çıkmak için q'ya basın)\033[0m\n{" "*35}")
        if a.lower() == "q":
            sys.exit(1)
        time.sleep(2)
        clear()
    
    def greetingScreen(self):
        time.sleep(1)
        EWriter.goodWriting("Merhaba oyuncu!")
        time.sleep(1)
        EWriter.goodWriting("İsmini öğrenebilir miyim?")
        while True:
            self.player_name = input("\t>>")
            if self.player_name:
                break
            else:
                EWriter.goodWriting("İsim yerine bir şey yazman lazım!")
                continue
        EWriter.goodWriting("\nHarika!")
        EWriter.goodWriting(f"Kuralalrı biliyor musun \033[1m{self.player_name}\033[0m?(e/h)")
        while True:
            response = input("\t>>")
            if response:
                if not response.lower() in ["e","h"]:
                    EWriter.goodWriting("Kutucuğa 'e' veya 'h' yazman lazım!")
                    continue
                else:
                    break 
            else:
                EWriter.goodWriting("Kutucuğa 'e' veya 'h' yazman lazım!")
                continue
        if response.lower() == "h":
            EWriter.goodWriting("Peki,gelsin kurallar!")
            self.rulesScene()
        else:
            EWriter.goodWriting(f"Peki,bol şans \033[1m{self.player_name}\033[0m!")
    
    def rulesScene(self):
        time.sleep(1)
        EWriter.goodWriting("\nOyun başladığında ilk önce taş , kağıt veya makastan birini seçmelisin.")
        EWriter.goodWriting("Sonrasında bigisayarda taş kağıt ve makastan birini seçer.")
        EWriter.goodWriting("Unutma,taş makası,kağıt taşı,makasta kağıdı yener!")
        EWriter.goodWriting("Geri kalan tüm durumlar berabere olarak kabul edilir.")
        EWriter.goodWriting("3 kere yenen kişi kazanır(berabere puan vermeyecek.)")
        EWriter.goodWriting(f"Anladıysan bol şans \033[1m{self.player_name}\033[0m!")
        
    def gameScene(self):

        time.sleep(1)
        print()
        print("_"*90)
        print()
        EWriter.goodDialogue("COMPUTER","T(aş) mı K(ağıt) mı M(akas) mı?")
        while True:
            choice = input("\t>>")
            if choice:
                if not choice.lower() in ["t","k","m"]:
                    EWriter.goodDialogue("COMPUTER","Kutucuğa T(aş) K(ağıt) veya M(akas) yazman gerek!")
                    continue
                else:
                    break
            else:
                EWriter.goodDialogue("COMPUTER","Kutucuğa T(aş) K(ağıt) veya M(akas) yazman gerek!")
                continue
        convert_map = {
            "t" :1,
            "k" :2,
            "m" :3,
        }
        choice = convert_map[choice.lower()]
        computer_choice = random.randint(4,6)
        EWriter.goodDialogue("COMPUTER","Taş..",end="")
        EWriter.goodWriting("Kağıt..",end="")
        EWriter.goodWriting("Makas..")
        print("\n")
        time.sleep(1)
        self.resultScreen(choice,computer_choice)

App = Game()
App.mainMenu()
App.greetingScreen()

while True:
    App.gameScene()
    if App.playerScore >= 3:
        EWriter.goodDialogue(f"COMPUTER",f"Tebrikler \033[1m{App.player_name}\033[0m!",end="")
        EWriter.goodWriting(" Kazandın!",duration=0.07)
        App.playerScore = 0
        App.computerScore = 0
    elif App.computerScore >= 3:
        EWriter.goodDialogue("COMPUTER",f"Maalsef kaybettin \033[1m{App.player_name}\033[0m!",end="")
        EWriter.goodWriting(" Bir daha ki sefere :(",duration=0.07)
        App.playerScore = 0
        App.computerScore = 0
    else:
        continue
    
    EWriter.goodDialogue(f"COMPUTER",f"Tekrar oynamak ister misin \033[1m{App.player_name}\033[0m?",end="")
    EWriter.goodWriting(" Bu sefer kesin yeneceğim(e/h)!",duration=0.07)
    
    while True:
        response = input("\t>>")
        if response:
            if not response.lower() in ["e","h"]:
                EWriter.goodWriting("Kutuya bir şey yazman lazım!",duration=0.05)
                continue
            elif response.lower() == "e":
                time.sleep(0.2)
                break
            else:
                EWriter.goodDialogue(f"COMPUTER",f"Korkak!",duration=0.1)
                time.sleep(1)
                App.mainMenu()
                
        else:
            EWriter.goodWriting("Kutuya bir şey yazman lazım!",duration=0.05)   
            continue
        