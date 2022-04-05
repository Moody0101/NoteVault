"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

This file is for variables, functions and things to use in the project.
Author: Moody0101

Note:
	I used : 'SHA256'
	You can change the hashing algorithm to the following:
		{'sha3_224', 'sha1', 'sha384', 'sha512', 'blake2s', 'md5', 'shake_256', 'sha3_384', 'sha224', 'sha3_512', 'shake_128', 'sha3_256', 'blake2b'}

	I used: 'BASE64'
	You can change the encoding algorithms to the following:
		{'Base32', 'Base16', 'Base85'}

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from base64 import ( b64encode, b64decode )
from hashlib import sha256
from os import path
from vars import LIGHTCYAN_EX

# HELPING FUNCTIONS.
def encode_(s: str) -> str: return b64encode(s.encode()).decode()

def decode_(s: str) -> str: return b64decode(s.encode()).decode()

def hash_(s: str) -> str: return sha256(s.encode()).hexdigest()

def verifypassword(p: str, hash_: str) -> bool: return sha256(p.encode()).hexdigest() == decode_(hash_)

def store(fileName: str, s: str) -> bool:
	try:
		with open(fileName, 'w') as f:
			f.write(f"\n{encode_(s)}")
		return 1
	except:
		return 0

def read(fileName: str) -> bool:
	try:
		i = 0
		with open(fileName) as f:
			for s in f.readlines()[1:]:
				print(f"\n({i}) {decode_(s)}")
				i += 1
			if i == 0:
				print(f"{LIGHTCYAN_EX}LOOKS EMPTY FOR NOW!")
		return 1
	except:
		return 0

def exists(DIR: str) -> bool: return path.exists(DIR)



if __name__ == '__main__':
	[print(x) for x in dir(sha256('s'.encode())) if not str(x).startswith('__')]


