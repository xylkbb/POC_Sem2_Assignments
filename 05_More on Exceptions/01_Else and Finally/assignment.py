def Calc():
    test = int(input("(first number -->)  "))
    test2 = int(input("Divided by  "))

    a = test
    b = test2
    
    work = a / b
    print(work)

# ----------------------------------------------------------- #

try:
    Calc()
except ValueError:
    print("You need to input a number")
    
    
except ZeroDivisionError:
    print("Dividing by 0 is a nono")
    
else:
    print('Everything Above Worked')
finally:
    print(" ^^ Complete ^^ ")