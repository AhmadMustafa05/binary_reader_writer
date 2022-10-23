import pickle

def overwriteonit(file):
    areyousureaboutit=input("This will overwrite everything do you want to continue? Y or N:")
    if areyousureaboutit=="N":
        exit()
    print("This will overwrite whatever there is on the file!!")
    thetypeofthing=input("Enter what type of entry you have string or a number: ")
    if thetypeofthing=="string":
        thething=input("Enter the string: ")
    elif thetypeofthing=="number":
        thething=float(input("Enter the number:" ))


    try:
        pickle.dump(thething, file)

    except EOFError:
        file.close
    return

