prime = 5
modulus = 23
a = 4
b = 3 
A = pow(prime,a)%modulus
B = pow(prime,b)%modulus
print(A, B)
aconfirm = pow(B,a)%modulus
bconfirm = pow(A,b)%modulus
print(aconfirm, bconfirm)