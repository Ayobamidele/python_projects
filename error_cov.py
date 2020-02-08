x = 24
y = "0"

print("Hey")

try:
    print(x / y)
except ZeroDivisionError and TypeError as c:
    print("Hey, this number cannot be divided by zero")
else:
    print("somethig else went wrong")
finally:
    print("This is my clean up code")

print("bye")