num=int(input("enter a number : "))
if num<=1:
    print(f"{num}  is not a prime number")
elif num%2==0 and num !=2:
     print(f"{num} is not a prime number")
    
else:
    for i in range(3,num):
        if num%i==0:
            print(f"{num}  is not a prime number")
            break
    else:
        print(f"{num}  is a prime number")
