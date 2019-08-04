import os
from os import system
from utils.generic import clear_output
from time import sleep

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
# print(list_dot_files)


def add_command_alias():
    """
    Adds alias to .bashrc
    :return: None
    """
    os.chdir("~")
    dot_files = list_dot_files()
    if ".bashrc" in dot_files:
        cwd = os.getcwd() + "/.main.py"
        system('echo "alias pull=""python"{}"'.format(cwd))
        clear_output()
        print("Added command alias to .bashrc")
    else:
        clear_output()
        print("It seems as though there is no .bashrc file located in your root.")
        make_bashrc = input("Should we make a new one in root?\n")
        if "y" in make_bashrc:
            system("touch .bashrc")
            clear_output()
            print("Created bashrc")
        else:
            clear_output()
            print("The application can't run without that alias being added to the .bashrc")
            print("This means that the application will stop in 20 seconds")
            for i in range(20):
                sleep(1)
                print(20 - i)


