import codecs
import os
import Exit


def zapisanie_notatki():

    name = input("Podaj tytuł notatki: ")
    AppRunning = True

    try:
        # Sprawdź, czy folder "Notes" istnieje, jeśli nie, utwórz go
        if not os.path.exists("Notes"):
            os.makedirs("Notes")
        # Sprawdź, czy plik .txt istnieje, jeśli nie, utwórz go
        lista_plikow = os.listdir("Notes")
        if lista_plikow:
            # Sprawdź, czy plik .txt o takiej nazwie istnieje, jeśli nie, utwórz go
            for plik in lista_plikow:
                if plik == name + ".txt":
                    print("Error: Plik o takiej nazwie już istnieje.")
                    AppRunning = False
                    Exit.continue_app()
        if AppRunning == True:
            with codecs.open(os.path.join("Notes/", name + ".txt"), 'w', "utf-8"):
                print("Utworzono nowy plik o nazwie: ", name + ".txt")

    except Exception as error_name:
        print(f"Wystąpił błąd: {str(error_name)}")

    note = input("Twoja notatka: \n")
    try:
        with codecs.open(os.path.join("Notes/", name + ".txt"), 'w', "utf-8") as f:
            f.write(note)
    except Exception as error_name:
        print(f"Wystąpił błąd: {str(error_name)}")

    print("\nNotatka zapisana.")
