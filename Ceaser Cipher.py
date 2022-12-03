def encrpytion(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if(char==' '):
            result+=' '
        elif (char.isupper()):
            result += chr((((ord(char)-65)+shift)%26)+65)
        else:
            result += chr((((ord(char)-97)+shift)%26)+97)
    return result

def decrpytion(encrpytedtext, shift):
    result = ""
    for i in range(len(encrpytedtext)):
        char = encrpytedtext[i]
        if(char==' '):
            result+=' '
        elif (char.isupper()):
            result += chr((((ord(char)-65)-shift)%26)+65)
        else:
            result += chr((((ord(char)-97)-shift)%26)+97)
    return result
text=input().strip()
shift=int(input())
encrpytedtext=encrpytion(text, shift)
decrpytedtext=decrpytion(encrpytedtext, shift)
print("Plain Text : "+text)
print("The shift : "+str(shift))
print("The Encrypted Text: "+encrpytedtext)
print("The Decrypted Text: "+decrpytedtext)