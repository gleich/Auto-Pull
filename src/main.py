import os
import argparse
from os import system

import commands
from utils import timer


def config_warning():
    """
    Warns the user how they haven't run the config command yet.
    """
    print("It seems as though you haven't ran the config command.\nPlease run that first\nThe program will stop in 10 seconds. Please restart.")
    timer.countdown(10)


def main():
    """
    Runs the whole program
    """
    parser = argparse.ArgumentParser(
        description="Tool for pulling from all of your Git repos")
    parser.add_argument("-c", "--config", type=str, metavar="",
                        help="Edit the settings for the tool")
    parser.add_argument("-r", "--run", type=str,
                        metavar="", help="Runs the program")
    args = parser.parse_args()
    while True:
        if args.config is not None:
            cwd = os.getcwd()
            commands.add_command_alias()
            github_folders_location = "./" + \
                input("What is the location of your Git folders?\nKeep in mind that the program still works if their are files/folders located in that folder that aren't related to Git.\nPlease make sure that the path is relative to the root.\n\n~/")
            try:
                os.listdir(github_folders_location)
            except FileNotFoundError:
                print(
                    "It seems as though that folder doesn't exist.\nThe program will restart in 5 seconds.")
                timer.countdown(5)
                continue
            while True:
                try:
                    with open("auto_pull_config.txt", "w") as config_file:
                        github_folder_location_line = "git_folder_location=" + github_folders_location
                        config_file.write(github_folder_location_line)
                    print("Successfully configured the program. You can now run the tool from anywhere using `pull <command>`\nThe program will now stop, please restart")
                except FileNotFoundError:
                    system("touch auto_pull_config.txt")    
                    continue
                break
            break
        elif args.run is not None:
            try:
                with open("auto_pull_config.txt") as config_file:
                    file_contents = config_file.read()
                settings_list = {}
                file_lines = file_contents.split("\n")
                for line in file_lines:
                    key_value_pair = line.split("=")
                    settings_list[key_value_pair[0]] = key_value_pair[1]
                if "git_folder_location" not in settings_list.keys():
                    config_warning()
                print(settings_list["git_folder_location"], "This was gotton from the file. It works!")
                break
            except FileNotFoundError:
                config_warning()
                continue


main()
