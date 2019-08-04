import os
import argparse

def main():
    """
    Runs the whole program
    """
    parser = argparse.ArgumentParser(description="Tool for pulling from all of your Git repos")
    parser.add_argument("-c", "--config", type=str, metavar="", help="Edit the settings for the tool")
    parser.add_argument("-r", "--run", type=str, metavar="", help="Runs the program")
    args = parser.parse_args()
    if args.config is not None:
        print("Looks like you are gonna configure the system")
    elif args.run is not None:
        print("Looks like you wanna run the program")

main()