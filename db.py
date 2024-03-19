import os

def addKey(key, value):
    if os.path.exists(key):
        with open(key, 'r') as file:
            with open(key, 'w') as file:
                file.write(value)
    else:
        with open(key, 'w') as file:
            file.write(value)

addKey("len", "2")
