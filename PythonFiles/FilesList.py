import os
import textwrap
import DEV


def wypisz_spis_plikow():
    try:
        if os.path.exists("Notes") and os.path.isdir("Notes"):
            lista_plikow = os.listdir("Notes")

            if lista_plikow:

                text = textwrap.fill(f'{"Data utworzenia":<30}{"Znaki":<10}{"Nazwa":<20}\n')
                print(text)

                for plik in lista_plikow:
                    utworzono = DEV.note_time(plik)
                    znaki = DEV.note_stats(plik)

                    text = textwrap.fill(f'{utworzono}{"    "}{znaki:<10}{''.join(os.path.splitext(plik)[0]):<20}\n')
                    print(text)

            else:
                print("Brak notatek. ")

    except Exception as error_name:
        print(f"Wystąpił błąd: {str(error_name)}")
