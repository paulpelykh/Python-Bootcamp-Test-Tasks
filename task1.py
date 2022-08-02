import hashlib

s = "Python Bootcamp"

def hash_string(string: str):
    return hashlib.sha256(str.encode('utf-8')).hexdigest()

print(hash_string(s))