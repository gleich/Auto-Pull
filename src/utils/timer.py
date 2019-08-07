import time

def countdown(seconds):
    """
    A countdown that prints out how many seconds are left
    :param seconds: number of seconds in the count down
    :return: None
    """
    for i in range(seconds):
        time.sleep(1)
        print(seconds - i)