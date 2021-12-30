import os
import json

print("Save directory in JSON file")
# TODO: napisać program który pobierze zawartość folderu i zapisze jego zawartość w pliku json
# zapis (nazwy plików rozszerzenia rozmiar datę utworzenia pliku!)
# odczyt
# zapytania największe pliki najnowsze czy pliki z konkretnym rozszerzeniem

cwd = os.getcwd() #current directory
os.chdir(cwd)
#print(cwd)
path=cwd+'/'+json_folder_name
if os.path.isdir(path):
    shutil.rmtree(path)
os.mkdir(json_folder_name)


with open("/path/to/file.json", "w+") as f:
    json.dump(object_to_write, f)
