import hashlib
from crypto.Hash import SHA
from crypto.PublicKey import DSA
import libnum, random



def nonce(alice, bob):
	a = libnum.s2n(alice[:8]) 
	s = libnum.s2n(bob[:4]) 
	random.seed(a^s) 
	return a*s + random.randint(a+s,a*s)


pub = DSA.import_key((open("public.pem").read()))

PNG_HEADER = bytes.fromhex('89504e470D0A1A0A')
JPG_HEADER = bytes.fromhex('FFD8ffE0')
k = nonce(PNG_HEADER, JPG_HEADER)

m1 = open("signed.txt","rb").read()
h1 = SHA.new(m1).digest()
r1 = pow(pub.g,k,pub.p) % pub.q

orig_r, orig_s = (39293439036445053408522626936142807124096433248296453702500722051098852055379, 33846259599286415849820644741398830119755847893862372378624889039917194176541)

x = ((orig_s * k) % pub.q - libnum.s2n(h1)) * libnum.invmod(r1, pub.q) % pub.q

def sign_msg(msg):
	h = SHA.new(msg).digest()
	r = pow(pub.g,k,pub.p) % pub.q
	s = libnum.invmod(k,pub.q)*(libnum.s2n(h) + x * r) % pub.q
	sig = (r,s)
	return sig

m2 = open("need_to_sign.txt","rb").read()

r,s = sign_msg(m2)

print(f'BreakALLCTF{{{hashlib.md5(str(r+s).encode()).hexdigest()}}}')




#BreakALLCTF{31737080fa4c2b586d91dcf79e25b284}
