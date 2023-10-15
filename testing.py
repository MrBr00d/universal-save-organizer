import pathlib
import os
import pickle
class Testing:
    var1 = []
    def __init__(self, name):
        Testing.var1.append(name)


# a = Testing("Hello")
# b = Testing("World")

# print(Testing.var1)

def to_pickle(object, pickle_pth):
    pickle_pth = pathlib.Path(pickle_pth)
    pickle_data = pickle.dump(object)
    pickle_pth.write_bytes(pickle_data)