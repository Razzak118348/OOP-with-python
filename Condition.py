#membership operator(in not in) , identity operator(is is not)

a = input("Enter a number: ")
a = int(a)
if a > 5:
    print(f'{a} number is greater than 5')
elif a == 5:
    print(f"{a} number is equal to 5")
else:
    print(f"{a} number is less than 5")



age = int(input("Enter your age: "))

if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")
