#1
# artist = input("What is your favourite artist?: ")
# compliment = "is brilliant"
# print(artist +(" ") + compliment)

#2

# fullName = input("what is your full name?: ")
# fName = fullName.index(" ")
# fName = fullName[:fName]
# print(fName)
# sName = fullName.index(" ")
# sName = fullName[sName+1:]
# print(sName)

#3
print("Please enter the time: 9hrs 52 mins 18secs")
hours = int(input("hours:"))
minutes = int(input("minutes:"))
seconds = int(input("Seconds:"))
totalHours = (hours*60*60)
totalMinutes = (minutes*60)
print(totalHours + totalMinutes + seconds)
