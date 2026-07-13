"""
Pythondan basit bir sayı tahmin oyunu yapımı.

Örnek Çıktı:
sen : 6
cevap : aşağı
sen : 4
cevap : yukarı
sen : 5
cevap : DOĞRU!

"""
import time
import random
def goodWriting(text:str,duration=0.05,end="\n"):
    for i in text:
        print(i,end="",flush=True)
        time.sleep(duration)
    print("",end=end)

def goodDialogue(name,text:str,duration=0.05,end="\n"):
    print(f"{name} :",end="")
    goodWriting(text,duration,end=end)
class NGG():
    def __init__(self,aiName = "Bilgisayar",letterDuration = 0.05):
        self.player_name = "Oyuncu" 
        self.aiName = aiName
        self.winCount = 0
        self.loseCount = 0
        self.recor = 0
    def greetingScreen(self):
        def rulesScene():
            goodWriting("\nİlk önce bilgisayar 1 ve 100 arasında(1 ve 100 dahil) bir sayı seçer.")
            time.sleep(0.2)
            goodWriting("Sonrasında sen bu sayıyı tahmin etmeye çalışırsın!",end=" ")
            time.sleep(0.3)
            goodWriting("Eğer sayın hedeften küçükse sana 'Sayıyı Azalt' diye uyarı verilir.",end="")
            goodWriting("Büyükse 'Sayıyı Büyült' diye bir uyarı verir!")
            goodWriting("Sayıyı bilmen için toplam 5 hakkın var.")
            goodWriting("Bol şans!\n")
        print("<--- Sayı Tahmin Oyunu --->")
        goodWriting("\nMerhaba oyuncu,lütfen ilk önce ismini gir!",0.05)
        self.player_name = input("\t>>")
        goodWriting(f"\nGüzel isim , şimdi oyuna başlamadan önce bir şey sormam lazım {self.player_name}!")
        goodWriting(f"Kuralları biliyor musun(e/h)?")
        response = input("\t>>")
        if response.lower() == "e":
            goodWriting("Güzel!")
            goodWriting("O zaman kuralları geçiyorum , bol şans!")
        
        elif response.lower() == "h":
            goodWriting("O zaman gelsin kurallar!")
            time.sleep(1)
            rulesScene()
        
        else:
            goodWriting("Geçersiz cevap,ama kuralları biliyorsun sayacağım.")
            goodWriting("Bol şans!")
        time.sleep(3)
        print(f"\n{50*"*"}\n")
    def game(self):
        randomNumber = random.randint(1,100)
        chance = 5
        goodDialogue(self.aiName,"Sayıyı seçtim , bakalım bulabilicek misin?\n")
        while True:
            try:
                playerChoice = int(input(f"{self.player_name} :"))
            except ValueError:
                goodDialogue(self.aiName,"Hahaha,aptal!",end=" ")
                time.sleep(0.2)
                goodWriting("Sayı girmen lazım.")
                continue
            
            if playerChoice < 0 or playerChoice > 100:
                goodDialogue(self.aiName,"Hahaha,aptal!",end=" ")
                time.sleep(0.2)
                goodWriting("kuralları okumadın galiba.")
                continue
            
            if playerChoice == randomNumber:
                goodDialogue(self.aiName,"Tebrikler!",end=" ")
                time.sleep(0.4)
                goodWriting("Sayıyı bulabildin.")
                self.winCount += 1
                break
            
            elif playerChoice < randomNumber:
                chance -= 1
                goodDialogue(self.aiName,f"Sayıyı büyültmen lazım , {chance} hakkınız kaldı.")
                
            elif playerChoice > randomNumber:
                chance -= 1
                goodDialogue(self.aiName,f"Sayıyı küçültmen lazım , {chance} hakkınız kaldı.")
                
            if chance == 0:
                goodDialogue(self.aiName,"Maalsef hakkınız bitti,",end=" ")
                time.sleep(0.4)
                goodWriting("bir dahaki sefere tekrar deneyin!")
                goodDialogue(self.aiName,f"Bu arada sayı '{randomNumber}' sayısıydı.")
                self.loseCount += 1
                break

App = NGG("AI")
App.greetingScreen()
while True:
    App.game()
    goodWriting("\nBir daha oynamak ister misin(e/h)?")
    response = input("\t>>")
    if response.lower() == "e":
        continue
    else:
        goodWriting(f"Görüşürüz {App.player_name}!")
        break
    

