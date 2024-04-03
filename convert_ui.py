import os
import subprocess
from os import listdir

from PyQt6.uic import pyuic


def convert_ui():
    for file in listdir("designs"):
        if file[-3:] == ".ui":
            # subprocess.run(["pyuic6", f"designs/{file}", "-o", f"pages/{file[:-3]}.py"], capture_output=True)
            # subprocess.run(["echo", "\"Hello World!\""])
            pyuic.generate(f"designs/{file}", f"pages/{file[:-3]}.py", 0, None)


if __name__ == '__main__':
    convert_ui()
