x = 10
y = x
print(id(x) == id(y))

x += 1
print(id(x) == id(y))

z = 10
print(id(z) == id(y))
