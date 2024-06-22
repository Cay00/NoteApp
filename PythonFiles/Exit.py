import os
import sys


def continue_app():

    print(" ")
    wejscie = input("Czy chcesz kontynuować? (y/n): ")
    if wejscie == 'y':
        print("")
        os.system("cls")
    elif wejscie == "n":
        sys.exit()
    else:
        print("Wybrano błędną opcję!")


def break_app():

    if input("Czy aby na pewno chcesz wyjść? (y/n): ") == 'y':
        sys.exit()
    else:
        print("")
        os.system("cls")
