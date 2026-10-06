#tasks pg42 and pg43
#1

noList = []
for i in range(5):
    num = int(input("Enter a number: "))
    noList.append(num)
    
print(noList)
q  = (0)
for i in range(5):
    no = noList[q]
    no = no + 1
    q = q+1
    print(no)


#2
# hours = [12,7,9,9,6,8,2]
hours = []
for i in range(7):
    hours.append(int(input("Enter hours for each day spent at home: ")))
    
print(hours)    

l2 = 1
total = hours[0]
for i in range(6):
    l2 = l2
    total = total + hours[l2]
    l2 += 1

print(total,"litres")
pay = total*1.35
pay = round(pay,ndigits = 3)
print("€",pay)


#3
#adding all together
rain = []
for i in range(7):
    rain.append(float(input("Enter rain for each day : ")))    
print(rain)        
r2 = (1)
total1 = rain[0]
for i in range(6):
    r2 = r2
    total1 = total1 + rain[r2]
    r2 += 1
print("total rainfall this week: ",total1,"cm")

#average
total2 = total1 / len(rain)
total2 = round(total2,ndigits = 3)
print("average rainfall this week:",total2,"cm")

#Seeing if it was greater than 3.5cm
days = ["Monday","Tuesday","Wedsday","Thursday","Friday","Saturday","Sunday"]
dig = (0)
for i in range(7):
    if rain[dig] >= 3.5:
        print(days[dig],"was very wet!")
        dig += 1
    else:
        dig += 1
        

#4
saleP = int(input("enter the amount of salepersons: "))
pers = []
made = []
for i in range(saleP):
    pers.append(input("Enter your name : "))  
    made.append(float(input("Enter how much you made: ")))
print(made)
print(pers)




p = 0
m = 0
for i in range(saleP):
    p = p
    m = m
    print(pers[p],"made: €",made[m])
    p += 1
    m += 1
    
tp = (1)
total = made[0]
for i in range(saleP-1):
    tp = (tp)
    total = total + made[tp]
    tp += 1
print("total earnings: €",total)
   
#max/min
m2 = 1
currentMin = []
Min = []
for i in range(saleP-1):
    if made[0] >= made[m2]:
        currentMin.append(m2)
        Min = currentMin[-1]
        m2 += 1
    else:
        m2 += 1        
print(pers[Min],"made the least")    
    
m3 = 1
currentMax = []
Max = []
for i in range(saleP-1):
    if made[0] <= made[m3]:
        currentMax.append(m3)
        Max = currentMax[-1]
        m3 += 1
    else:
        m3 += 1
print(pers[Max],"made the most")

average = total / len(pers)
average = round(average,ndigits = 3)
print("average: ",average,"cm")
