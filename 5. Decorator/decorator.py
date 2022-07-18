import datetime

ab = []

def decorators(func):
    def wraper(*args):
        beginning = datetime.datetime.today().strftime("Дата: %Y %m %d Время: %H:%M:%S")
        name_func = func
        argument = args
        retur = func(*args)

        print(f"\nНачало работы функции {beginning}")
        print(f"Имя функции: {name_func}")
        print(f"Функции передан аргумент: {argument}")
        print(f"Вывод значений: {retur}", "\n\n" + "*"*100)

        ab.append(f"Начало работы функции в {beginning} Имя функции: {name_func} Функции передан аргумент: {argument} Возвращаемое значение: {retur}""")

        with open("text.txt", "w") as txt:
            txt.write(str(ab))

        return func(*args)
    return wraper