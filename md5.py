import hashlib
message = input("enter the message : ").strip()
result = hashlib.md5(message.encode())
print("The hexadecimal equivalent of hash is : ", end ="")
print(result.hexdigest())