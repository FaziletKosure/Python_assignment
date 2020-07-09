number = int(input("Enter a number please : "))

if number % 2 == 0 and number != 2:
    print(f"{number} is not a prime number")
else:
    for i in range(3, number, 2):
        if number % i == 0:
            print(f"{number} is not a prime number")
            break
    else:
        print(f"{number} is  a prime number")
