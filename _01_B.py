
a = int(input("Enter a number: "))

if (a%2 == 0):
    if a%3 == 0:
        print("Yes, the number is odd and divisible by 3")
    else:
        print("!!!!")
else:
    print("The number is even")