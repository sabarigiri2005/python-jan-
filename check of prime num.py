a=int(input())
for i in range(2,a):
    if a % i ==0:
        temp = 0
        print("Its not a prime number :(")        
        break
    else:
        temp=1

if temp == 1:
    print("Its a prime number :)")
