import os
import textwrap
import DEV
import Fav

def wypisz_spis_plikow():

    try:
        if os.path.exists("Notes") and os.path.isdir("Notes"):
            lista_plikow = os.listdir("Notes")
            if lista_plikow:
                text = textwrap.fill(f'{"Data utworzenia":<30}{"Nazwa":<15}{"Znaki":<10}\n')
                print(text)
                for plik in lista_plikow:
                    utworzono = DEV.note_time(plik)
                    znaki = DEV.note_stats(plik)
                    text = textwrap.fill(f'{utworzono}{"    "}{"".join(os.path.splitext(plik)[0]):<15}{znaki:<10}\n')
                    print(text)
                print("")
            else:
                print("Brak notatek. ")
    except Exception as error_name:
        print(f"Wystąpił błąd: {str(error_name)}")

def wypisz_ulubione():
    try:
        if os.path.exists("Notes") and os.path.isdir("Notes"):
            lista_plikow = filter(Fav.is_fav, os.listdir("Notes"))
            if lista_plikow:
                text = textwrap.fill(f'{"Data utworzenia":<30}{"Nazwa":<15}{"Znaki":<10}\n')
                print(text)
                for plik in lista_plikow:
                    utworzono = DEV.note_time(plik)
                    znaki = DEV.note_stats(plik)
                    text = textwrap.fill(f'{utworzono}{"    "}{"".join(os.path.splitext(plik)[0]):<15}{znaki:<10}\n')
                    print(text)
                print("")
            else:
                print("Brak ulubionych notatek. ")
    except Exception as error_name:
        print(f"Wystąpił błąd: {str(error_name)}")