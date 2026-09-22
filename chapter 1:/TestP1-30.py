# #last question google forms
# score = int(input("Please Enter the house score: "))
# if (score <= 10):
#      print("Energy Rating = F")
# elif(score <= 20):
#     print("Energy Rating = E")
# elif(score <= 30):
#     print("Energy Rating = D")
# elif(score <= 40):
#     print("Energy Rating = C")
# elif(score <= 70):
#     print("Energy Rating = B")
# else:
#     print("Energy Rating = A")

#1
cinemaName = "tralee movie house"
print(cinemaName)
#2
name = input("enter your full name: ")
age = int(input("enter your age: "))
amount = int(input("How may tickets do you want to buy: "))
cost = float(input("price of one ticket: "))
#3
tCost = cost * amount + 2
print(tCost)
#4
if (amount % 2)== 0 :
    pairs = ("Tickets can be split into pairs.")
else:
    pairs =("There will be one ticket left over.")
#5
lName = len(name)
print(lName)
#6
extract = name[0:3]
print(extract)
#7
sAge = str(age)
ref = extract+sAge
print("Your booking refrence is",ref)
#8
if age < 13:
    ticket = ("Child ticket")
elif age <= 17:
    ticket = ("Teen ticket")
else:
    ticket = ("Adult ticket")
#9
print("")
print("") 
print("----BOOKING SUMMARY----")
print("Customer: ",name)
print("Number of tickets: ",amount)
print("Price per ticket: $",cost)
print("Total ticket cost: $",tCost-2)
print("Booking fee: $2")
print("Final cost: $",tCost)
print("Cost per person: $",tCost/amount)
print("Name length: ",lName)
print("First three charachters: ",extract)
print("Booking refrence: ",ref)
print("Ticket type: ",ticket )
print(pairs)
   
