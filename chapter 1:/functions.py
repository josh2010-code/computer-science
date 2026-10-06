#Function basic
def calcSpeed(d,t):
    speed = d/t
    return speed
print("-----Average Speed Calculator-----")
distance = int(input("Enter the distance in meters: "))
time = int(input("Enter the time in seconds: "))
avg = calcSpeed(distance,time)
print("The average speed is",round(avg,2))
