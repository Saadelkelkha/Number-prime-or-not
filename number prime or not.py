N=int(input("type the number :"))
ND = 0
for D in range (1,N+1):
    if N % D == 0 :
       ND = ND + 1
    if ND == 2 :
       print("the number is prime")
    else :
       print("the number is not prime")   