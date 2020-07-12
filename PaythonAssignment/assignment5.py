fibonacci = []
x = 1
y = 1

while x <= 55:
    fibonacci.append(x)
    x, y = y, x + y
print('till 55 fibonacci : ', fibonacci)
