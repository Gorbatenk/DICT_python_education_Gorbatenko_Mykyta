"""Главный сценарий арифметическая тестовая игра"""
from random import randint, choice
from time import sleep

data = {
    "score": 0,
    "level": 0,
    "right": 0,
    "name": ""
}

description_level = [
    "1 - simple operations with numbers 2-9",
    "2 - squaring numbers 2-9"
]


def save_result_in_file():
    """
    Сохраните результаты игры игрока в файл.

    Эта функция предлагает игроку ввести свое имя и возвращает текущий уровень игры.
    Затем он сохраняет результаты игрока (количество правильных ответов из 5 и уровень сложности) и
    описание уровня в файл с именем "results.txt".
    """
    print("What is your name?")
    description = description_level[data['level'] - 1].split(" - ")[1]
    with open("results.txt", "a") as f:
        f.write(f"Name: {data['right']}/5 in level {data['level']} ({description})\n")
    print("The results are saved in 'results.txt'.")


def formula_created(rank: int) -> str:
    """
    Сгенерируйте математическую формулу для заданного уровня сложности.

    Параметры:
        rank (int): уровень сложности игры.

    Возвращает:
        str: Строковое представление математической формулы.
    """
    array_symbols = ["-", "+", "*"]
    result = ""
    symbol_choice = choice(array_symbols)
    if rank == 1:
        result += str(randint(2, 9)) + symbol_choice + str(randint(2, 9))
    elif rank == 2:
        result += f"{randint(2, 9)}**2"

    return result


def processing(formula: str) -> None:
    """
    Обработайте ввод игрока для заданной математической формулы.

    Параметры:
        формула (str): математическая формула для обработки ввода игрока.
    """
    while True:
        try:
            input_user = int(input("> "))
            if eval(formula) == input_user:
                print("Right!")
                data["right"] += 1
                return
            else:
                print("Wrong!")
                return
        except ValueError:
            print("Incorrect format. Try again.")


def main():
    """Основная функция для арифметической тестовой игры."""
    print("""Which level do you want? Enter a number:""")
    print(*description_level, sep="\n")
    data['level'] = int(input("\nInput level: "))
    while True:
        if data["score"] >= 5:
            print(f"Your mark is {data['right']}/5.")
            print("Would you like to save your result to the file? Enter yes or no.")
            if input(">").strip() in ["yes", "1"]:
                save_result_in_file()
            exit(0)

        formula = formula_created(data['level'])
        print("\n" + formula)
        processing(formula)
        data["score"] += 1
        sleep(1)


if __name__ == '__main__':
    main()
