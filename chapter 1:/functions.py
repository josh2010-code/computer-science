#Function basic
def calcSpeed(d,t):
    speed = d/t
    return speed
print("-----Average Speed Calculator-----")
distance = int(input("Enter the distance in meters: "))
time = int(input("Enter the time in seconds: "))
avg = calcSpeed(distance,time)
print("The average speed is",round(avg,2))



# #Function basic
# def calcSpeed(d,t):
#     speed = d/t
#     return speed
# print("-----Average Speed Calculator-----")
# distance = int(input("Enter the distance in meters: "))
# time = int(input("Enter the time in seconds: "))
# avg = calcSpeed(distance,time)
# print("The average speed is",round(avg,2))



    
#1. Can you work out what is happening here?
print ("----AVERAGE SPEED CALCULATOR----")
#2. Find out what does "def" mean ?
def calculate(d, t):
    speed = d / t
    return speed

def checkSpeedLimit(speed):
    limit = 30  # speed limit in m/s
    if speed > limit:
        print("you are breaking the law")
        
    else:
        print("Good boy")

def timeTake(d,s):
   time = d/s
   return time     
    
    
# 1. Get input from the user
distance = int(input("Enter the distance travelled in metres: "))
time = int(input("Enter the time it took to complete the journey in seconds: "))
while time == 0:
    time = int(input("zero doesnt work, enter a new number: "))
    

# 2. Calculate the average speed
avgSpeed = calculate(distance, time)
print("The average speed is:", round(avgSpeed, 2), "m/s")
print("-----------------------------------")  # Prints a divider line

checkSpeedLimit(avgSpeed)


time = timeTake(1000,avgSpeed)
print(round(time),"seconds to travel 1000 meters")

 
'''Challenge 3: Convert to km/h
Average speed in meters per second (m/s) can be hard to visualize for cars. Create a function that converts avgSpeed into kilometers per hour (km/h).
Hint: To convert m/s to km/h, multiply the speed by 3.6.
Round to 2 dp
'''
def kilometers(t):
    km = t*3.6
    return km
   
k = kilometers(avgSpeed)
print(avgSpeed,"is",k,"km/h")    
'''Challenge 4: What could crash the programme?
Can you fix?
'''
