#membership operator(in not in) , identity operator(is is not)

a = input("Enter a number: ")
a = int(a)
if a > 5:
    print(f'{a} number is greater than 5')
elif a == 5:
    print(f"{a} number is equal to 5")
else:
    print(f"{a} number is less than 5")

name = False
if name is not True:
    print('name is not True')
    #nested if else
    if 8%2 == 0:
        print('8 is even')
    else:
        print('8 is odd')

else:
    print('name is True')