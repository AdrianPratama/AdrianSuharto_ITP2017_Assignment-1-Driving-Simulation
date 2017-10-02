change = input("Please input the order of the swapping:")#asking for the swapping order
new_list = list(change)#creating a list for the values inputted in change
a,b,c = 1,0,0 #initial position of the ball
for i in new_list: #for loop until the last order is achieved
    if i.upper()=="A":
        a,b = b,a #swapping the value of a and b
    elif i.upper()=="B":
        b,c = c,b #swapping the value of b and c
    elif i.upper()=="C":
        a,c = c,a #swapping the value of c and a
    else:
        print("Unidentified pattern!") #if the order is incorrect
print(a,b,c)#print the final spot of the ball, signified by the number 1
