word = input("Enter a single alphabet: ")

encrypt =(ord (word) - 97) % 26 + 97

print(f"The encrypted output is: " + str(encrypt))
