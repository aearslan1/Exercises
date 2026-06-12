"""
Pythodan basit bir to-do-list uygulaması.
örnek çıktı:
menü:
1-görev ekle
2-listele
3-işaretle
4-sil
5-çık

1 işaretlendiğinde
ne eklemek istesiniz

"""

import os
import sys
import json

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def createFolder(folder_name):
    main_path = sys.argv[0]
    folder_path = os.path.dirname(main_path)
    join_path = os.path.join(folder_path,folder_name)
    print(folder_path)
    if not os.path.exists(join_path):
        os.mkdir(join_path)

def printMiddle(stringLen:int,text:str):
    print(" "*((stringLen-len(text))//2) + text + " "*((stringLen-len(text))//2))

clear()
createFolder("data")

class TDLApp():
    def __init__(self):
        
        self.main_path = os.path.dirname(os.path.abspath(__file__))
        self.database_path = os.path.join(self.main_path,"data","database.json")
        if not os.path.exists(self.database_path):
            with open(self.database_path,"w") as file:
                file.write("{}")
        with open(self.database_path,"r",encoding="utf-8") as file:
            try:
                json_content = json.load(file)
            except:
                json_content = None
        self.data = json_content
        
        
        
    def add(self,duty:str):
        if not duty in self.data:
            self.data[duty] = False
        with open(self.database_path,"w",encoding="utf-8") as file:
            json.dump(self.data,file,indent=4,ensure_ascii=False)
    
    def listData(self):
        data_pack = ""
        def convertBox(statue:bool):
            if statue:
                return "[x]"
            return "[]"
        for order,duty in enumerate(self.data):
            data_pack += f"{order+1}-{duty} -> {convertBox(self.data[duty])}\n"
        return data_pack

    def delete(self,dutyIndex:int):
        keys = list(dict(self.data).keys())    
        del self.data[keys[dutyIndex]]
        with open(self.database_path,"w",encoding="utf-8") as file:
            file.write(json.dumps(self.data,ensure_ascii=False,indent=4))

    def checkDuty(self,dutyIndex:int):
        keys = list(dict(self.data).keys())    
        self.data[keys[dutyIndex]] = not self.data[keys[dutyIndex]]
        with open(self.database_path,"w",encoding="utf-8") as file:
            file.write(json.dumps(self.data,ensure_ascii=False,indent=4))
    def menu(self,indent=4):
        print("<Menü>")
        options = ["1. Görevleri Listele","2. Yeni Görev Ekle","3. Görevi Tamamlandı/Tamamlanmadı Yap","4. Görev Sil","5. Ekranı Temizle","6. Menüyü Aç","7. Çık"]
        for i in options:
            print(f"{indent * " "}{i}")
        

print("=== To-Do-List Uygulaması ===\n")
App = TDLApp()

App.menu()
while True:
    choice = input(">> ")
    if (choice == "1"):
        print("─" * 60)
        if App.listData():
            print(f"\n{App.listData()}")
        else:
            printMiddle(60,"BOŞ")
        print("─" * 60)
    
    elif(choice == "2"):
        print("─" * 60)
        print("<Görev Ekleme>")
        while True:
            added_duty = input(" -Görev adı(iptal etmek için hiç bişey yazmayıp onaylayın): ")
            if added_duty.strip():
                App.add(added_duty)
                print("<Görev başarıyla eklendi>")
            else:
                print("<Görev ekleme iptal edildi>")
                break
        print("─" * 60)
    
    elif(choice == "3"):
        print("─" * 60)
        print("<Görev İşaretleme>")
        while True:
            duty_number = input(" -Görev numarası(iptal etmek için hiç bişey yazmayıp onaylayın veya geçersiz bir değer yazın('a' gibi)): ")
            if duty_number.strip():
                try:
                    App.checkDuty(int(duty_number) - 1)
                except KeyError , TypeError ,ValueError , IndexError:
                    print("<Görev işaretleme iptal edildi>")
                    break
                print("<Görev başarıyla işaretlendi>")
            else:
                print("<Görev işaretleme iptal edildi>")
                break
        print("─" * 60)
    
    
    elif(choice == "4"):
        print("─" * 60)
        print("<Görev Silme>")
        will_be_deleted = []
        while True:
            def delete(delete_list:list):
                if delete_list:
                    delete_list.sort(reverse=True)
                    for element in delete_list:
                        App.delete(element)
            duty_number = input(" -Görev numarası(iptal etmek için hiç bişey yazmayıp onaylayın veya geçersiz bir değer yazın('a' gibi)): ")
            try:
                duty_number = int(duty_number)
            except ValueError:
                print("<Görev silme iptal edildi>")
                delete(will_be_deleted)
                break
            if duty_number > len(App.data) or duty_number < 1:
                        print("<Görev silme iptal edildi>")
                        break
            if str(duty_number).strip():
                try:
                    if int(duty_number) - 1 in will_be_deleted:
                        print("<Bu değeri zaten sildiniz>")
                        continue
                    will_be_deleted.append(int(duty_number) - 1)
                    
                except IndexError , ValueError , TypeError :
                    print("<Görev silme iptal edildi>")
                    delete(will_be_deleted)
                    break
                print("<Görev başarıyla silindi>")
            else:
                print("<Görev silme iptal edildi>")
                delete(will_be_deleted)
                break
        print("─" * 60)

    elif(choice == "5"):
        clear()
        
    elif(choice == "6"):

        print("─" * 60)
        App.menu()
    
    elif(choice == "7"):
        clear()
        break
    else:
        print("<Geçersiz Opsiyon>")
        continue # gene başa dönüyo ama daa sağlıklı genede(bence)
    