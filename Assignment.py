
time = int(input("Please input the time spent on the road: "))
acceleration = int(input("Please input the acceleration of the vehicle: "))
distance = int(input("Please input the distance of the destination: "))
velocity = 0

for i in range(time):
    while velocity < 60:
        velocity = velocity + acceleration

for j in range (11):
    star = (j*j*2)//10
    print("Duration: "+str(j)+ " Distance:"+star*"*")

if time * acceleration>60:
    print("\nThe person went over the speed limit: (Max speed was " +str(time*acceleration)+"m/s)\n")
else:
    print("\nThe person did not go over the speed limit: (Max speed was " +str(time*acceleration)+"m/s)\n")

check = (acceleration*time*time/2) - distance
if check >= 0:
    print("The person reached the destination. (Reached " +str(distance)+"m")
else:
    print("The person did not reach the destination. (Reached "+str(distance + check)+"m")
