import pickle
def readit(file):
    i=True
    try:
        while i==True:
            output=pickle.load(file)

            print(output)
    except EOFError:
        file.close
    return

