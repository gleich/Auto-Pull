import os
from os import system
from time import sleep

from utils.generic import clear_output
from utils import timer

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
    orig_cwd = os.getcwd()
    print(orig_cwd)
    for i in range(orig_cwd.count("/") - 2):
        os.chdir("..")
    dot_files = list_dot_files()
    if ".bashrc" in dot_files:
        alias = 'alias pull="cd .' + orig_cwd + ' && python main.py -run && cd ~"'
        print(alias)
        system('echo "{}" >> .bashrc'.format(alias))
        clear_output(20)
        print("Added command alias to .bashrc")
    else:
        clear_output(20)
        print("It seems as though there is no .bashrc file located in your root.")
        make_bashrc = input("Should we make a new one in root?\n")
        if "y" in make_bashrc:
            system("touch .bashrc")
            clear_output(20)
            print("Created bashrc")
        else:
            clear_output(20)
            print("The application can't run without that alias being added to the .bashrc")
            print("This means that the application will stop in 20 seconds")
            timer.countdown(20)


