import hashlib

def encrypt(password): 
    encoded = password.encode() 
    passwordEncrypted = hashlib.sha256(encoded)
    return passwordEncrypted.hexdigest()
#def
