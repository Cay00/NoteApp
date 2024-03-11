import Zapis
import Odczyt
import Yeet
import Exit
import FilesList
import DEV

# zapisywanie krótkich notatek (aplikacja do zapisywania tekstu brudnopis) #

AppRunning = True

while bool(AppRunning):
    print("\nZapisywanie notatek")
    print("1. Napisz notatkę")
    print("2. Otwórz notatkę")
    print("3. Usuń notatkę")
    print("4. Wypisz pliki")
    print("5. Zakończ")
    print("10. Dev (Utwórz nowy plik o treści Lorem Ispum)\n")
    mode = input("Podaj numer funkcji: ")

    match mode:
        case "1":
            Zapis.zapisanie_notatki()
            Exit.continue_app()

        case "2":
            FilesList.wypisz_spis_plikow()
            Odczyt.odczytanie_notatki()
            Exit.continue_app()

        case "3":
            FilesList.wypisz_spis_plikow()
            Yeet.remove()
            Exit.continue_app()

        case "4":
            FilesList.wypisz_spis_plikow()

        case "5":
            Exit.break_app()

        case "10":
            DEV.lorem_note()
            Exit.continue_app()

        case _:
            print("~")
            print("Error: Wybrano niewłaściwą opcję!")
            print("~")
