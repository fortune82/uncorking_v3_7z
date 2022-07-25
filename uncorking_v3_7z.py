import py7zr
# секундомер. Необходимо установить (pip install stopwatch.py)
from stopwatch import Stopwatch
import time  # для создания эффекта печатания текста с задержкой
# для созлания разноцветного текста в программе
from colorama import init, Fore, Back, Style
init()


def console_picture():
    print(Style.BRIGHT + Fore.WHITE)
    print("   ########   ########  ##      ##   #######   ########    ######## ")
    print("   ########   ########  ##      ##   ##    ##  ##          ######## ")
    print("   ##    ##   ##    ##  ##     ###   ########  ########       ##  ")
    print("   ##    ##   ########  ##  ##  ##   ##    ##  ##             ##  ")
    print("   ##    ##   ##        ## #    ##   ########  ########       ##  ")
    print("   ##    ##   ##        ##      ##   #######   ########       ##  ")
    print()
    print()
    print("   ########      ###    ##      ##   ########   ##      ##  ########     @@ ")
    print("   ##           #####   ##      ##   ##    ##   ##      ##  ########     @@ ")
    print("   ######      ##   ##  ##########   ##    ##   ##      ##     ##        @@ ")
    print("   ##    ##   ##     ## ##      ##   ##    ##   ##    ####     ##        @@ ")
    print("   ########   ######### ##      ##   ##    ##   ##  ##  ##     ##        @@ ")
    print("   ######     ##     ## ##      ##  ##########  ## #    ##     ##           ")
    print("                                    ##      ##  ##      ##     ##        @@ ")
    print()
    print()
    print()


console_picture()


wordTitle = '          Программа для взлома запароленных 7z архивов '
# создаем эффект печатания текста (текст выводиться с задержкой)
for i in wordTitle:
    print(i.upper(), end="")
    time.sleep(0.03)

print(Style.BRIGHT + Fore.RED)
print()
print("Предупрежение!")
print()
print("""Файлы с таким расширением очень устойчивы к атакам грубой силы, 
поэтому перебор паролей будет происходить крайне низко!!!""")

stopwatch = Stopwatch(2)  # 2 это десятична точность для секундомера


def crack_password(password_list, file_for_breaking):
    indx = 0
    cnt = len(list(open(password_list, 'rb')))
    # открываем файл (with open() as file: - пишем так, чтобы потом не писать комманду закрытия файла (close()). rb открытие в двоичном режиме )
    with open(password_list, 'rb') as file:
        stopwatch.restart()
        for line in file:
            for word in line.split():
                # вычисляем в процентном соотношении количество пребранных паролей
                x = (indx+1)/cnt * 100
                # отсекаем цифры после запятой до 2-х, чтоб не получалось вроде такого: 0.9834539503%
                x = float('{:.2f}'.format(x))
                print(
                    f'Количество перебранных паролей {indx} ----- Процент перебранных паролей {x} ---- Прошло времени {str(stopwatch)}\r', end="")  # подсчитываем количество перебранных паролей. Вывод текста в одну строку с затиранием предыдущего
                try:
                    indx += 1
                    with py7zr.SevenZipFile(file_for_breaking, password=word.decode('utf8')) as z:
                        z.extractall()
                    print("\n")
                    print(Style.BRIGHT + Fore.GREEN)
                    print("Пароль найден в строке: ", indx)
                    # Декодирует байтстроку в строку.
                    print("Пароль: ", word.decode())
                    stopwatch.reset()  # сбрасываем счетчик на 0
                    # После нахождения пароля, спрашиваем про желание продолжить взламывать пароли
                    continue_work = input(
                        "Хотите продолжить? Если да, то нажмите букву 'д'")
                    if (continue_work == 'д'):
                        main_data()
                        # return True
                    else:
                        return True

                except:

                    continue
    return False


def main_data():
    print(Style.BRIGHT + Fore.YELLOW)
    archive_file = input("\nВведите адрес 7z архива ")
    # делаем проверку рассширенния взламываемого файла
    if not archive_file.endswith(('.7z')):
        print(Style.BRIGHT + Fore.RED)
        print("Вы указали неверный файл. Файл не имеет расширения '7z' ")
        main_data()

    password_list = input("Введите адресс словаря ")

    file_for_breaking = archive_file

    # подсчитываем количесвто слов в словаре
    cnt = len(list(open(password_list, 'rb')))

    print("Количество паролей в данном словаре ", cnt)

    if crack_password(password_list, file_for_breaking) == False:
        print("\nПароль не найден. Попробуйте другой словарь ")
        main_data()


main_data()
