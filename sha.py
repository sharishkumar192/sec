import hashlib
text = hashlib.sha1(b'cryptography')
encrypt = text.hexdigest()
print(encrypt)