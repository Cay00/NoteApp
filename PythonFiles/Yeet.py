import os


def remove():
    try:
        if os.path.exists("Notes") and os.path.isdir("Notes"):
            lista_plikow = os.listdir("Notes")

            if lista_plikow:
                name = input("Wybierz plik, który chcesz usunąć: ")
                sciezka = os.path.join("Notes", name + ".txt")

                os.remove(sciezka)
                print("Notatka o nazwie " + name + ".txt została pomyślnie usunięta.")

    except Exception as error_name:
        print(f"Wystąpił błąd: {str(error_name)}")
        # print("Error: Wystąpił błąd!")
