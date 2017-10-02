result = []#empty list to store the data
for i in range(0,10):#range of 10 for 10 integers
    integer = int(input())#asks for input from the user
    value=integer%42#finding the unique/non-unique value
    result.append(value)#appending the unique or non-unique value into the list
print(len(set(result)))#removing non unique value and finding the total number of unique value
