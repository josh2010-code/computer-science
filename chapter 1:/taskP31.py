# #4
print("Hello and welcome to the free ticket giver 2000!")
userNo = input("Enter a tram ticket number:A ,B or C : ")
userNo = userNo.lower()

if userNo == "a":
    print("Free ticket to Dundrum!")

elif userNo == "b":
    print("Free ticket to Tallaght")

elif userNo == "c":
    print("Free ticket to Broomsbridge")
    
else:
    print("Invalid entry!")
    
#5
grade = int(input("Enter your grade: "))

if grade <= 29:
    print("H8")

elif grade <= 39:
    print("H7")

elif grade <= 49:
    print("H6")
    
elif grade <= 59:
    print("H5")
    
elif grade <= 69:
    print("H4")
    
elif grade <= 79:
    print("H3")
    
elif grade <= 89:
    print("H2")
    
else:
    print("H1")
    
    

    
