import codecs
import os


def odczytanie_notatki():
    name = input("Podaj tytuł notatki: ")

    try:
        with codecs.open(os.path.join("Notes/", name + ".txt"), 'r', "utf-8") as odczyt:
            odczyt = odczyt.read()

            print(odczyt)

    except Exception as error_name:
        print(f"Wystąpił błąd: {str(error_name)}")
        # print("Error: Brak pliku o takiej nazwie!")
