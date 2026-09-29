# #Basic for loops

# for y in range(1,5):
#     print(y)
# 
# for y in range(1,5):
#     print(y)
# for y in range(1,5):
#     print(y)
# print(y)
# 
# counter = 1
# while(counter<5):
#     print(counter)
#     counter+=1
# while(counter<5):
#     print(counter)
#     counter+=1
# print(counter)
# 
# for i in range(1,6):
#     print(i)
# c=1
# while(c<=5):
#     print(c)
#     c+=1

# #more about the range func

# for i in range(71,50):
#     print(i,"st paddys")

##loop statements with for and strings

# inputText = "john28"
# for i in inputText:
#     print(i)
    
# sen = input("Enter")
# spaceCount = 0
# for charachter in sen:
#     if charachter ==" ":
#         spaceCount+=1
# wordCount = spaceCount+1
# print(spaceCount)
# print(wordCount)

# sen = input("Enter")
# spaceCount = 0
# c = 0
# while c <len(sen):
#     if sen[c] == " ":
#         spaceCount+=1
#     c+=1
# wordCount = spaceCount+1
# print(spaceCount)
# print(wordCount)

#T1
"""for i in range(1,11):
    print(i)
c = 1
while (c<=10):
    print(c)
    c+=1 

#T2
num = int(input("enter a number"))
for i in range(1,num+1,2):
    print(i)


#T3
string = "Hi my name is josh"
string = string.lower()
count = 0
for c in string:
    if c == "a" or c=="u" or c=="o" or c== "i" or c=="e":
        count+=1
print(count)
