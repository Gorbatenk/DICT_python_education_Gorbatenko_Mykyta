import sys
import random


def lucky_process(amount_user, names, price, amount):
    """Функция Удачи в случае выбора Нет процесс продолжаеться
    при выборе ДА 1 человек(рандомно)убираеться из расчёта"""

    print("Do you want to use the \"Who is lucky?\" feature? Write Yes/No:")
    luck_input = str(input('>'))
    while luck_input != "luck_input":
        if luck_input == "No":
            print("No one is going to be lucky")
            dict_1 = dict.fromkeys(names, price)
            print(dict_1)
            sys.exit('See you next time !_!')
        elif luck_input == "Yes":
            lucky_user = random.choice(names)
            print(lucky_user + "is the lucky one!")
            new_price = amount / (amount_user - 1)
            dict_1 = dict.fromkeys(names, new_price)
            dict_1[lucky_user] = 0
            print(dict_1)
            sys.exit('Goodbye!')

def get_dictionary():
    """Функция просит ввести данные после чего выводить значения ключа.
    Делает основной расчёт"""

    names = []
    print("Enter the number of friends joining (including you)")
    amount_user = int((input(">")))
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(amount_user):
        names.append(str(input(">")))
    if amount_user == 0:
        sys.exit("No one is joining for the party):")
    dict_1 = dict.fromkeys(names, 0)
    print(dict_1)
    print("Enter the total amount:")
    amount = float(input(">"))
    price = amount / amount_user
    dict_1 = dict.fromkeys(names, round(price, 2))
    print(dict_1)
    lucky_process(amount_user, names, price, amount)


get_dictionary()
