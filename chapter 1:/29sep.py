"""
#2
shopping = []
shopping.append("banana")
shopping.append("chocolate")
shopping.append("car")
for i in range(4):
    item = input("enter an item: ")
    shopping.append(item)
print(shopping)
#2
t = ["lions","tigers","bears"]
t[1] = "eagles"
i  = input("enter a team name")
t[0] = i
print(t)
#3
names = ["ada","josh","sam","joe"]
print(names[2])
print((names[0]),(names[3]))


#4
b = ["a1","b2","c3","d4"]
print(b[-1])
print(b[-2])

#5
mon = ["jan","feb","mar","apr","may"]
print(mon[1:4])
print(mon[:2])

#6
s = ["cork","mallow","limerick","ennis"]
print(s[1:])
print(s[-2:])


#7
c = ["wash","dry","fold","store"]
del c[1]
del c[-1]
print(c)
#8

#9
n = ["dune","holes"]
n.extend(["wonderful"])
ne = ["book","BOOK"]
n.extend(ne)
print(n)

#10
r  = ["run","shower"]
r.insert(0 ,"warmup")
print(r)
l = (len(r))
r.insert(l,"cooldown")
print(r)
 """
#11
          
col = ["red","blue","green","blue"]
col.remove("blue")







col.remove("blue")
print(col)

