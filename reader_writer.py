import pickle
from overwrite_func  import overwriteonit
from write_func import writeonit
from read_func import readit

print("This is a program to read and write in a binary file!")

action=input("Do you want to read or write or overwrite?: ")

if action=="overwrite":
    file=open(r"/Users/mustafa/Developer/Code/Code/Python/Own Projects/binary_reader_writer/binary_storage/newfile.bin", "wb")
    overwriteonit(file)

if action=="write":
    file=open(r"/Users/mustafa/Developer/Code/Code/Python/Own Projects/binary_reader_writer/binary_storage/newfile.bin", "ab")
    writeonit(file)
if action=="read":
    file=open(r"/Users/mustafa/Developer/Code/Code/Python/Own Projects/binary_reader_writer/binary_storage/newfile.bin", "rb")
    readit(file)
