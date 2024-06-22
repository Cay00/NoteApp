import codecs
import os
import Yeet
import FilesList


def odczytanie_notatki():

    try:
        if os.path.exists("Notes") and os.path.isdir("Notes"):
            lista_plikow = os.listdir("Notes")
            # Sprawdź, czy notatki istnieją, jeśli nie, utwórz jedną
            if lista_plikow:
                FilesList.wypisz_spis_plikow()
                name = input("Podaj tytuł notatki: ")
                try:
                    with codecs.open(os.path.join("Notes/", name + ".txt"), 'r', "utf-8") as odczyt:
                        odczyt = odczyt.read()
                        print(odczyt)
                except Exception as error_name:
                    print(f"Wystąpił błąd: {str(error_name)}")

                # Menu po wyświetleniu notatki
                print("1. Edytuj    2. Dodaj do lubionych    3. Usuń")
                mode = input("Podaj numer funkcji: ")

                match mode:
                    case "1":
                        print("Nie wspierane")
                    case "2":
                        print("Nie wspierane")
                    case "3":
                        Yeet.remove(name)
            else:
                print("Brak notatek. ")
    except Exception as error_name:
        print(f"Wystąpił błąd: {str(error_name)}")

