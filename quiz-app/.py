import time

print("--"*50, "\nЦе система приложення подготовки до тестів Python для початківців. Тут ви знайдете різні файли з кодом, які допоможуть вам вивчити основи програмування на Python.\n", "--"*50) # Це повідомлення виводиться на початку кожного файлу, щоб привітати користувача та надати інформацію про призначення цього файлу.
name=input("Як до вас можно звертатися? ")
print(f"Добре {name}")
age=int(input("Скільки вам років? "))
print(f"Добре {name}, вам {age} років")
city=input("В якому місті ви проживаєте? ")
print(f"Добре {name}, ви проживаєте в місті {city}")
menu=input(f"Вас звати: {name}\n Вам: {age} років\n Ви проживаєте в місті: {city}\n Все правильно? (так, ні) \n")
def total():
    while menu == "так":
        print(f"Добре {name}!)")
        Action=input("Виберіть дію: (1-Тест, 2-Про мене, 3-Вихід)")
        if Action == "1":
                time.sleep(3)
                test1=input("\nЯк називається команда в Python, яка дозволяє отримати дані від користувача через клавіатуру?\n (\na-print,\n b-input,\n c-scan) \nтільки цифри: ")
                if test1 == "b":
                    print("Правильно!")
                    bal1=1
                else:
                    print("Неправильно!")
                    bal1=0
                test2=input("\nЯка команда в Python використовується для виведення тексту на екран?\n (\na-print,\n b-input,\n c-scan) \nтільки цифри: ")
                if test2 == "a":
                    print("Правильно!")
                    bal2=1
                else:
                    print("Неправильно!")
                    bal2=0
                test3=input("\nЯка команда в Python використовується для отримання числа від користувача через клавіатуру?\n (\na-print,\n b-input,\n c-scan) \nтільки цифри: ")
                if test3 == "b":
                    print("Правильно!")
                    bal3=1
                else:
                    print("Неправильно!")
                    bal3=0
                test4=input("\nЯка команда в Python використовується для виведення тексту на екран?\n (\na-print,\n b-input,\n c-scan) \nтільки цифри: ")
                if test4 == "a":
                    print("Правильно!")
                    bal4=1
                else:
                    print("Неправильно!")
                    bal4=0
                wse=bal1+bal2+bal3+bal4
                if wse == 4:
                    print(f"Добре {name}")
                elif wse == 3:
                    print(f"Добре {name}")
                elif wse == 2:
                    print(f"Тримально{name}")
                elif wse ==1:
                    print(f"Погано{name}")
                elif wse == 0:
                    print(f"Погано{name}")
                else:
                    print(f"Помилка{name}")
                break
        elif Action == "2":
                print(f"\n Ваше імя: {name}\n Ващи вік: {age}\n Ваше місто: {city}\n Ваш розвязок: {wse}\n")
        elif Action == "3":
            print("Папа!")
            break
if menu == "так":
    total()
print("-"*50, f"\n Добре {name}!", "-"*50)
