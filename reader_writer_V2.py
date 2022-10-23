import pickle
import os
import sys
from overwrite_func  import overwriteonit
from write_func import writeonit
from read_func import readit

i=True

while i==True:
    storagee=open(os.path.join(sys.path[0], "current_locations.txt"), "r+")

    print("This is a program to read and write in a binary file!")

    print("Last entered locations: ")
    print(storagee.readline())

    x=input("Enter the file location: ")
    storagee.truncate(0)

    storagee.write(x)

    storagee.close()

    action=input("Do you want to read or write or overwrite?: ")

    if action=="overwrite":
        file=open(x, "wb")
        overwriteonit(file)

    if action=="write":
        file=open(x, "ab")
        writeonit(file)
    if action=="read":
        file=open(x, "rb")
        readit(file)
    exitsure=input("Exit? Y or N: ")
    if exitsure=="Y" or exitsure=="y":
        exit()
    elif exitsure=="N" or exitsure=="n":
        continue
