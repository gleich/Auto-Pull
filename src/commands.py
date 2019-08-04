import os
from os import system

def list_dot_files():
    """
    List all dot files
    :return: list of dot files
    """
    files = os.listdir()
    dot_files = []
    for file in files:
        characters_of_file_name = list(file)
        if "." == characters_of_file_name[0]:
            dot_files.append(file)
    return dot_files

# Testing
print(list_dot_files)


def add_command_alias():
    os.chdir("~")
    dot_files = list_dot_files()
    if ".bashrc" in dot_files:
        os.system()