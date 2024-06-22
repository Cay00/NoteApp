import Zapis
import Odczyt
import Yeet     #usuniencie plików#
import Exit     #zakończenie programu z poziomu funkcji#
import FilesList
import DEV      #funkcja twożąca gotową notatkę do testowania#
import Fav

AppRunning = True

while bool(AppRunning):
    print("\nZapisywanie notatek")
    print("1. Napisz notatkę")
    print("2. Otwórz notatkę")
    print("3. Usuń notatkę")
    print("4. Wypisz pliki")
    print("5. Dodaj notatke do ulubionych")
    print("6. Wyświetl ulubione")
    print("9. Zakończ")
    print("10. Dev (Utwórz nowy plik o treści Lorem Ispum)\n")
    mode = input("Podaj numer funkcji: ")

    match mode:
        case "1":
            Zapis.zapisanie_notatki()
            Exit.continue_app()

        case "2":
            Odczyt.odczytanie_notatki()
            Exit.continue_app()

        case "3":
            FilesList.wypisz_spis_plikow()
            Yeet.remove(input("Wybierz plik, który chcesz usunąć: "))
            Exit.continue_app()

        case "4":
            FilesList.wypisz_spis_plikow()

        case "5":
            Fav.favourite()

        case "6":
            FilesList.wypisz_ulubione()

        case "9":
            AppRunning = False

        case "10":
            DEV.lorem_note()
            Exit.continue_app()

        case _:
            print("~")
            print("Error: Wybrano niewłaściwą opcję!")
            print("~")
