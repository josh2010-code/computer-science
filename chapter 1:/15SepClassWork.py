# blackCoffee = 5
# whiteCoffee = 10
# print(blackCoffee > whiteCoffee)
# 
# blackCoffee = 5
# whiteCoffee = 10
# print((blackCoffee == 6) and (whiteCoffee==10))
# 
# blackCoffee = 5
# whiteCoffee = 10
# print((blackCoffee != 6) or (whiteCoffee==10))
# 
# blackCoffee = 5
# whiteCoffee = 10
# print(not(blackCoffee > 6) and (whiteCoffee==10))

username = "axl@gunsnroses.com"
password = "novemberrain"
username1 = input("enter username: ")
password1 = input("enter password: ")
if ((username == username1) and (password == password1)) :
    print("correct")
else:
    print("wrong password or username dweeb!:(")
print("Welcome to the driving licence eligibilty checker")

age = int(input("what age are you?: "))
#it is requesting an input from the user as an integer
name = input("what is ur name?: ")
#question 16 a iii
print("you entered",age)
if ((age >= 17) and (age <=74)) :
    print("you can apply",name)

elif (age > 74) :
    print("you can apply for a three year licence",name)
else :
    print(name,",you are not eligable")
    


#b
print("Split bill calculater")
bill = int(input("Total amount of the bill: "))
people = int(input("How many people: "))
owe = bill/people
print(owe)
