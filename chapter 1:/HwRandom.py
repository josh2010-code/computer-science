from random import randint
a = 1
rList = []
while a<4:
    number = (randint(1,99))
    a += 1
    rList.append(number)
print(rList)
inumber = int(input("Enter your lucky number between 1 and 99"))
N = 0
for i in range(len(rList)):
    if inumber == rList[N]:
        print(inumber,"Was correct")
        N+=1
        break
#if inumber == rList[0] or rList[1] or rList[2] or rList[3] or rList[4]
    
