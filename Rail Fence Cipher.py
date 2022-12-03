def printtable(table):
    result=""
    for i in range(len(table)):
        for j in range(len(table[0])):
            if(table[i][j]!=' '):
                result+=table[i][j]
    return result
def encrpytion(text, shift):
    table = [ [" " for j in range(len(text))]for i in range(shift)]
    result = ""
    row = 0 
    flag = 0 
    for i in range(len(text)):
        table[row][i] = text[i]
        if(row==0):
            flag=1
        elif(row==shift-1):
            flag=0
        if(flag==1):
            row+=1
        else:
            row-=1
    return printtable(table)
    
text=input().strip()
shift=int(input())
encrpytedtext=encrpytion(text, shift)
print("Plain Text : "+text)
print("The shift : "+str(shift))
print("The Encrypted Text: "+encrpytedtext)