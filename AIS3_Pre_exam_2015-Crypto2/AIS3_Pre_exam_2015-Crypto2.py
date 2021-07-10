from os import read
from Crypto.Util.number import inverse, bytes_to_long, long_to_bytes


n = 66473473500165594946611690873482355823120606837537154371392262259669981906291
e = 65537

p = 800644567978575682363895000391634967
q = 83024947846700869393771322159348359271173

assert n ==p*q

phi = (p-1)*(q-1)
d = inverse(e, phi)


with open('flag.enc', 'rb') as f:
    c = f.read()
    c = bytes_to_long(c)
    m = pow(c, d, n)
    print(long_to_bytes(m))


#AIS3{rsaaaaaaaaA_orz}
