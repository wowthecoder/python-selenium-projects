import os
import shutil

path = "C:/Users/User/AppData/Local/Temp"
dir_list = os.listdir(path)

for folder in dir_list:
    if folder.startswith("scoped_dir"):
        shutil.rmtree(os.path.join(path, folder))
        print("Folder deleted: ", folder)

