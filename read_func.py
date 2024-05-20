import pickle
from colorama import Fore
def readit(file):
    i=True
    print(Fore.BLUE + "-----------------------\n" + ":       Result       :\n" + "-----------------------")
    print(Fore.WHITE + "\n")
    try:
        while i==True:
            output=pickle.load(file)
            print(output)
    except EOFError:
        file.close
    return

