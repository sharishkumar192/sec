def encrpytion(text, key):
   k = 0 
   texttable=[]
   keytable=[]
   ciphertable=[]
   result=""
   for i in range(3):
      l=[]
      for j in range(3):
         l.append(ord(text[k])-65)
         k+=1
      texttable.append(l)

   for i in range(3):
      keytable.append(ord(key[i])-65)

   for i in range(3):
      temp = 0 
      for j in range(3):
         temp+= (texttable[i][j] * keytable[j])
      ciphertable.append(temp%26)

   for i in range(3):
      result+= chr(ciphertable[i]+65)
   return result


    
text=input().strip()
key=input().strip()
encrpytedtext=encrpytion(text, key)
#decrpytedtext=decrpytion(encrpytedtext, key)
print("Plain Text : "+text)
print("The Key : "+key)
print("The Encrypted Text: "+encrpytedtext)
#print("The Decrypted Text: "+decrpytedtext)

#GYBNQKURP
#ACT