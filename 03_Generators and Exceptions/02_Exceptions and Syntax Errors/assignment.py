test = int(input("(first number -->)  "))
test2 = int(input("Divided by  "))

a = test
b = test2

try:
    work = a / b
    print(work)
except ZeroDivisionError:
    print("You're answer had the value '0' in it. You cannot divide by 0")
