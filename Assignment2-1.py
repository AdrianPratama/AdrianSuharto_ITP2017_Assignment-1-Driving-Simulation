names = input("Please input the names:") #ask for input from user
print(''.join(name[0] for name in (names.split("-"))))
#joining the first letter of the names.split list into an empty string using a for loop
