"""
Pythondan basit bir hesap makinesi.

Örnek Çıktı : 
a : 3
b : 5
işlem : +
sonuc = 8

""" 
def raiseError(text:str):
    print(f"\t{text}"+f"\n{(len(text) + 8)*"*"}\n")

def turnPure(number:float):

    if number.is_integer():
        return int(number)
    return number

print("<---Dört İşlemli Hesap Makinesi--->\n")
while True:
    number_1 = input("1.sayıyı giriniz :")
    try:
        number_1 = float(number_1)
    except ValueError:
        raiseError(f"'{number_1}' bir sayı değil , lütfen biri sayı giriniz.")
        continue
    
    operator = input("Bir işlem girin(+ - * /) :")
    if not operator in ["+","-","*","/"]:
        if operator == "q":
            break
        raiseError(f"'{operator}' tanımlanamayan bir işlem çeşidi , lütfen + - * / işlemlerini kullanın.")
        continue
    
    number_2 = input("2.sayıyı giriniz :")
    try:
        number_2 = float(number_2)
    except ValueError:
        raiseError(f"'{number_2}' bir sayı değil , lütfen biri sayı giriniz.")
        continue


    if operator == "+":
        result = number_1 + number_2
    elif operator == "-":
        result = number_1 - number_2
    elif operator == "*":
        result = number_1 * number_2
    elif operator == "/":
        if number_2 == 0:
            raiseError(f"sıfıra bölünme hatası , '{number_1}' sıfıra bölünemez.")
            continue
        result =  number_1 / number_2
        

    result_text = f"{turnPure(number_1)} {operator} {turnPure(number_2)} = {turnPure(result)}"
    print(f"\n{result_text}\n\n{len(result_text) * "*"}\n")