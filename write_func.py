import pickle
from colorama import Fore

def writeonit(file):
    print(Fore.BLUE + "-----------------------\n" + ":     Writer Menu    :\n" + "-----------------------")
    print(Fore.WHITE + "\n")
    thetypeofthing=input("Enter what type of entry you have string or a number? (S/N) ")
    if thetypeofthing=="S":
        thething=input("\nEnter the string: ")
    elif thetypeofthing=="N":
        thething=float(input("\nEnter the number:" ))
    print(Fore.RED + "\nWRITTEN!!!" + Fore.WHITE)
    try:
         pickle.dump(thething, file)

    except EOFError:
        file.close
    return
