x = int(input("x:   "))
y = int(input("y:   "))
z = 0

print("before the logic: ")
print("x:   ", x)
print("y:   ", y)

z = x
x = y
y = z

print("after the logic: ")
print("x:   ", x)
print("y:   ", y)
