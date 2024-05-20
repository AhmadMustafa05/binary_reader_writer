import pickle
from colorama import Fore
def overwriteonit(file):
    print(Fore.BLUE + "-----------------------\n" + ":     Reader Menu    :\n" + "-----------------------")

    areyousureaboutit=input(Fore.RED + "\nWARNING!!!!\n" + "This will overwrite everything do you want to continue? (Y/N)")
    if areyousureaboutit=="N":
        exit()
    print("This will overwrite whatever there is on the file!!\n")
    thetypeofthing=input(Fore.WHITE + "Enter what type of entry you have string or a number: (S/N) ")
    if thetypeofthing=="S":
        thething=input("\nEnter the string: ")
    elif thetypeofthing=="N":
        thething=float(input("\nEnter the number:" ))

    print("OVERWRITTEN!!")


    try:
        pickle.dump(thething, file)

    except EOFError:
        file.close
    return

