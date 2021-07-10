import base64
from pwn import *
from pwnlib.util.fiddling import xor

HOST = '120.114.62.215'
PORT = 4119
conn.remote(HOST,PORT)
conn.recvuntil('Here is your flag : ')
flag_cipher = base64.b64decode(conn.recvline().strip())

def getKey():
    conn.recvuntil('your turn : ')
    conn.sendline('blablabla')
    plain = "nonsensenonsense"
    cipher = base64.b64decode(conn.recvline().strip())
    key = xor(plain, cipher)
    return key

KeyList = []
for i in range(300):
    KeyList.append(getKey())
for key in KeyList:
    print(xor(flag_cipher, key))

#MyFirstCTF{XNiDNI0UO2jcFxmKr7Ur}
