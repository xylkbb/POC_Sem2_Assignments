
try:
    test = int(input("(first number -->)  "))
    test2 = int(input("Divided by  "))

    a = test
    b = test2
    
except ValueError:
    print("Number wasn't given")

try:
    work = a / b
    print(work)
except ZeroDivisionError:
    print("Dividing by 0 is a nono")