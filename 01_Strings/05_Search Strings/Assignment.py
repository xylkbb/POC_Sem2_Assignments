text = input("Enter some text: ")

checker = text.find('the')

if checker == -1:
    print("The word the is not in the strin")
else:
    print("The word the is is in the string")
    print("The word 'the' comes at", checker)