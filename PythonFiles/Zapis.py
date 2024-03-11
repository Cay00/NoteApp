import codecs
import os


def zapisanie_notatki():
    name = input("Podaj tytuł notatki: ")

    try:
        # Sprawdź, czy folder "Notes" istnieje, jeśli nie, utwórz go
        if not os.path.exists("Notes"):
            os.makedirs("Notes")

        with codecs.open(os.path.join("Notes/", name + ".txt"), 'w', "utf-8"):
            print("Utworzono nowy plik o nazwie: ", name + ".txt")

    except Exception as error_name:
        print(f"Wystąpił błąd: {str(error_name)}")
        # print("Error: Nazwa pliku ma zakazane znaki!")

    else:
        note = input("Twoja notatka: \n")
        try:
            with codecs.open(os.path.join("Notes/", name + ".txt"), 'w', "utf-8") as f:
                f.write(note)
        except Exception as error_name:
            print(f"Wystąpił błąd: {str(error_name)}")
            # print("Error: W pliku są zakazane znaki!")
        else:
            print("\nNotatka zapisana.")
