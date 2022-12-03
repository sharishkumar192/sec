def encrpytion(text, key):
    result = ""
    k = 0
    for i in range(len(text)):
       textint = ord(text[i])-65
       keyint = ord(key[k%len(key)])-65
       k+=1
       result += chr(((textint+keyint)%26)+65)
    return result

def decrpytion(encrpytedtext, key):
    result = ""
    k = 0
    for i in range(len(encrpytedtext)):
       textint = ord(encrpytedtext[i])-65
       keyint = ord(key[k%len(key)])-65
       k+=1
       result += chr(((textint-keyint)%26)+65)  
    return result
    
text=input().strip()
key=input().strip()
encrpytedtext=encrpytion(text, key)
decrpytedtext=decrpytion(encrpytedtext, key)
print("Plain Text : "+text)
print("The Key : "+key)
print("The Encrypted Text: "+encrpytedtext)
print("The Decrypted Text: "+decrpytedtext)