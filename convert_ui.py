import os
import subprocess
from os import listdir


def convert_ui():
    for file in listdir("designs"):
        if file[-3:] == ".ui":
            subprocess.run(["pyuic6.exe", f"designs/{file}", "-o", f"pages/{file[:-3]}.py"])


if __name__ == '__main__':
    convert_ui()
