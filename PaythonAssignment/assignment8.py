year = int(input('Enter a year in 4-digit format to check if leap or not : '))
if year % 4 == 0 and not year % 100 == 0 or year % 400 == 0:
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
