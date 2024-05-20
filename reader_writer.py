import pickle
import os
import sys
from colorama import Fore
from overwrite_func  import overwriteonit
from write_func import writeonit
from read_func import readit


i=True

while i==True:
    storagee=open(os.path.join(sys.path[0], "current_locations.txt"), "r+")
    print(Fore.CYAN + "\n##########################\n#  Binary reader/writer  #\n########################## \n ")
    print(Fore.GREEN + "-----------------------\n:    File selector    :\n-----------------------\n")
    print(Fore.WHITE + "Last entered file location: " + Fore.YELLOW + storagee.readline())
    #print(storagee.readline())
    print(Fore.WHITE + '\nCurrent working directory: ' + Fore.YELLOW + os.getcwd() + "\n")
    #print()
    fs = os.path.getsize(os.path.join(sys.path[0], "current_locations.txt"))
    if fs==0:
        print(Fore.RED + 'NO PREVIOUS DIRECTORY FOUND!')
        fils='N'

    else:
        fils=input(Fore.WHITE + "Do you want to use last location? (Y/N)")

    if fils=="Y":
        x=str(storagee)
    if fils=="N":
        x=input("\nEnter the file location: ")
        storagee.truncate(0)

        storagee.write(x)

        storagee.close()

    action=input("\nDo you want to read or write or overwrite?: (R/W/OW)")
    print("\n")

    if action=="OW":
        file=open(x, "wb")
        overwriteonit(file)

    if action=="W":
        file=open(x, "ab")
        writeonit(file)
    if action=="R":
        file=open(x, "rb")
        readit(file)
    exitsure=input("\nExit? (Y/N) ")
    if exitsure=="Y":
        exit()
    elif exitsure=="N":
        continue
