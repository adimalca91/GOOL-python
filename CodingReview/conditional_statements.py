user_input = input("Please Enter a Number: ")

if (len(user_input) == 2):
    print("2-digit number")
elif (len(user_input) == 3):
    print("3-digit number")
elif (len(user_input) == 4):
    print("4-digit number")
else:
    print("number is <= 9 || > 9999")

