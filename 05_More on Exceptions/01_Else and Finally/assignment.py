try:
    test = int(input("(first number -->)  "))
    test2 = int(input("Divided by  "))
except ValueError:
    print("An input was not correct")
else:
    print("No value error detected")
finally:
    print("Values taken care of")

try:
    a = test
    b = test2
    
    work = a / b
    print("The Answer is", work)
except ZeroDivisionError:
    print("Dividing by 0 is a nono")
    
else:
    print('Everything Above Worked')
finally:
    print(" ^^ Complete ^^ ")
