import os
import FilesList
import codecs

def favourite():
    if os.path.exists("Notes") and os.path.isdir("Notes"):
        lista_plikow = os.listdir("Notes")

        if lista_plikow:
            FilesList.wypisz_spis_plikow()
            name = input("Podaj tytuł notatki ktora chcesz dodac lub usunac z ulubionych: ")

            try: #zmienia nazwę ulubionej notatki dodając .f przed rozszeżeniem
                os.rename('Notes/' + name + '.txt', 'Notes/' + name + '.f' + '.txt')

            except:
                try: #jeśli notatka jest juz w ulubionych usuwa .f
                    os.rename('Notes/' + name + '.f' + '.txt', 'Notes/' + name + '.txt')
                except Exception as error_name:
                    print(f"Wystąpił błąd: {str(error_name)}")

def is_fav(n):
    x = ".f" in n
    return x