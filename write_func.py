import pickle

def writeonit(file):
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
