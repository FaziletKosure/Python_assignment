control_var = True

while control_var:
    number = input("Enter the number : ")

    if '.' in number:
        print("Please enter an integer number! ")
        continue
    elif number[0] == '-':
        print(" Please enter a positive number! ")
        continue
    elif not number.isdigit():
        print("Do not use any entries other than numeric values! ")
        continue

    else:
        control_var = False
n = len(number)
print(n)
sum_nth_pow = 0

for i in number:
    sum_nth_pow += int(i)**n
if int(number) == sum_nth_pow:
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")
