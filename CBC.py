import base64
from pwn import *
from pwnlib.util.fiddling import xor

#nc 140.110.112.215 4120
HOST = '140.110.112.215'
PORT = 4120
conn = remote(HOST, PORT)

line = conn.recvline().strip()
cipher = base64.b64decode(line)

IV, block1, block2, pad = cipher[:16], cipher[16:32], cipher[32:48], cipher[48:64]

zero = xor(block1, "A"*16)
payload = xor(zero, "CTFGOGOGO\x00\x00\x00\x00\x00\x00\x00")

result = b''.join([IV, payload, block2, pad])
output = base64.b64decode(result)

conn.sendline(output)
conn.interactive()
