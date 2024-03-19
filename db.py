import os
import rsa

publicKey, privateKey = rsa.newkeys(512)

def addKey(key, value):
    strKey = str(key)
    strVal = str(value)
    with open(strKey, 'w') as file:
        file.write(str(encrypt(strVal)))

def  readKey(key):
    strKey = str(key)
    if hasKey(strKey)==True:
        with open(strKey, 'r') as file:
            return decrypt(file.read())
    elif hasKey(strKey)==False:
        print("Key does not exist")
        return None
    
def addKeyUnsafe(key, value):
    strKey = str(key)
    strValue = str(value)
    with open(strKey, 'w') as file:
        file.write(strValue)

def  readKeyUnsafe(key):
    strKey = str(key)
    if hasKey(strKey)==True:
        with open(strKey, 'r') as file:
            return file.read()
    elif hasKey(strKey)==False:
        print("Key does not exist")
        return None

def deleteKey(key):
    if hasKey(key)==True:
        strKey = str(key)
        os.remove(strKey)
    elif hasKey(key)==False:
        print("Key does not exist")
        return None

def listKeys():
    return os.listdir()

def hasKey(key):
    strKey = str(key)
    if os.path.exists(strKey):
        return True
    else:
        return False

def encrypt(value):
    return rsa.encrypt(value.encode(),publicKey)

def decrypt(value):
    return rsa.decrypt(value, privateKey).decode()