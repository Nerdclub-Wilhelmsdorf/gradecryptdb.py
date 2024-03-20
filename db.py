import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

encryptKey = b'\x0f`\xf9g\x06\x19\x02\x19\xa24\xd6\x1a[\x89g\x80' #change key in production

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
    cipher = AES.new(encryptKey, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(value.encode('utf-8'))
    nonce = cipher.nonce

    save = str(nonce) + " " + str(ciphertext) + " " + str(tag)
    return save

def decrypt(save):
    save = save.split(" ")
    nonce = bytes(save[0],'utf-8')
    ciphertext = bytes(save[1], 'utf-8')
    tag = bytes(save[2], 'utf-8')
    cipher = AES.new(encryptKey, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    return data

def test():
    data = "test"
    return decrypt(encrypt(data)) == data