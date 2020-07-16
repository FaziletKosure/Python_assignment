prime_num = [2]
# we assume that user entered 100
n = int(input('Enter a number for prime calculation: '))
for x in range(1, n+1, 2):
    if x == 1:
        continue
    for y in range(3, x, 2):
        if x % y == 0:
            break
    else:
        prime_num.append(x)

print(prime_num)
