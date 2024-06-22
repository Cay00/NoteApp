import os
import codecs
import datetime


def lorem_note():

    try:
        # Sprawdź, czy folder istnieje, jeśli nie, utwórz go
        if not os.path.exists("Notes"):
            os.makedirs("Notes")
        # Utwórz plik txt w folderze z treścią Lorem Ipsum
        nazwa_pliku = os.path.join("Notes", "Lorem.txt")
        tresc_lorem_ipsum = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. 
Sed nisi. Nulla quis sem at nibh elementum imperdiet. Duis sagittis ipsum. Praesent mauris. Fusce nec tellus sed augue
semper porta. Mauris massa. Vestibulum lacinia arcu eget nulla. Class aptent taciti sociosqu ad litora torquent per
conubia nostra, per inceptos himenaeos. Curabitur sodales ligula in libero. Sed dignissim lacinia nunc. 

Etiam fringilla cursus enim, feugiat porttitor nulla lacinia vel. Nulla facilisi. Integer nec odio. Praesent libero.
Nulla facilisi. Ut sit amet convallis lacus. Nulla facilisi. Pellentesque dapibus efficitur laoreet. Proin volutpat
ex eu lacus condimentum, id posuere ligula vulputate. Vestibulum aliquet augue sit amet sodales imperdiet. Curabitur
nibh libero, tristique at dapibus a, scelerisque et risus.
"""
        with open(nazwa_pliku, 'w', encoding='utf-8') as plik:
            plik.write(tresc_lorem_ipsum)
        print(f"Plik 'Lorem.txt' został pomyślnie utworzony.")
    except Exception as error:
        print(f"Error: {str(error)}")


def note_stats(nazwa_pliku):

    try:
        with codecs.open(os.path.join("Notes/", nazwa_pliku), 'r', "utf-8") as plik:
            tresc = plik.read()
            return len(tresc)
    except Exception as error_name:
        print(f"Wystąpił błąd: {str(error_name)}")


def note_time(nazwa_pliku):
    try:
        with codecs.open(os.path.join("Notes/", nazwa_pliku), 'r', "utf-8"):
            time_create = os.path.getctime(os.path.join("Notes/", nazwa_pliku))
            data_utworzenia = datetime.datetime.fromtimestamp(time_create)
            return data_utworzenia

    except Exception as error_name:
        print(f"Wystąpił błąd: {str(error_name)}")
