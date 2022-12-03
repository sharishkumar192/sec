def encryption(text, key, noofcolumns):
	texttable=[['-']*noofcolumns for i in range(noofcolumns)]
	result=""
	k=0
	f=0
	for i in range(noofcolumns):
		temp=[]
		for j in range(noofcolumns):
			if(k!=len(text)):
				texttable[i][j]=text[k]
				k+=1
	for i in texttable:
	    print(*i)
	 
	for i in range(len(key)):
		for j in range(8):
		    #print(texttable[j][int(key[i])], end=" ")
		    #print(str(j)+""+str(int(key[i])), end=" ")
		    #print(i, end=" ")
		    if(texttable[j][int(key[i])]!='-'):
			    result+=texttable[j][int(key[i])]
	return result
#text = input().strip()
text="attackpostponeduntiltwoamxyz"
noofcolumns=8
key=[7, 0, 3, 6, 2, 5, 1]
print("The Key : ",*key)
print(len(text))
encryptedtext = encryption(text, key, noofcolumns)
print("Plain Text : "+text)
print("The Key : ",*key)
print("The Encrypted Text: "+encryptedtext)


#attackpostponeduntiltwoamxyz
#7
