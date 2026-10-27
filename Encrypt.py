from Crypto.Random import get_random_bytes
#RSA
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
def rsa_encrypt(message):
    key1=RSA.generate(2048)
    public1=key1.public_key()
    cipher1=PKCS1_OAEP.new(public1)
    encrypted1=cipher1.encrypt(message.encode())
    return encrypted1.hex()

#AES
from Crypto.Cipher import AES
def aes_encrypt(message):
    key2= get_random_bytes(32)
    cipher2=AES.new(key2,AES.MODE_GCM)
    encrypted2,tag1=cipher2.encrypt_and_digest(message.encode())
    return encrypted2.hex()

#DES
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
def des_encrypt(message):
    key3= get_random_bytes(8)
    cipher3=DES.new(key3,DES.MODE_CBC)
    padmsg=pad(message.encode(),DES.block_size)
    encrypted3=cipher3.encrypt(padmsg)
    return encrypted3.hex()

#HYBRID 
def hybrid_encrypt(message,algo):
    rsa_key=RSA.generate(2048)
    public2=rsa_key.publickey()
    if algo=="AES": 
        #AES
        key=get_random_bytes(32)
        cipher=AES.new(key,AES.MODE_GCM)
        encrypted,tag2=(cipher.encrypt_and_digest(message.encode()))
    elif algo=="DES":
        #DES
        key=get_random_bytes(8)
        cipher=DES.new(key,DES.MODE_CBC)
        padded=pad(message.encode(),DES.block_size) 
        encrypted=(cipher.encrypt(padded))
    rsa_cipher=(PKCS1_OAEP.new(public2))
    encrypted_key=(rsa_cipher.encrypt(key))
    return (encrypted.hex(),encrypted_key.hex())