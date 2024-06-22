import os


def remove(name):

    try:
        # Usuwanie notatki
        if os.path.exists("Notes") and os.path.isdir("Notes"):
            lista_plikow = os.listdir("Notes")
            if lista_plikow:
                sciezka = os.path.join("Notes", name + ".txt")
                os.remove(sciezka)
                print("Notatka o nazwie " + name + ".txt została pomyślnie usunięta.")
    except Exception as error_name:
        print(f"Wystąpił błąd: {str(error_name)}")
