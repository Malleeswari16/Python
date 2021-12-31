#Create a empty list
l1=[]
print(l1)
#Create a list with len 10.
l2=list([1,7,89,345,78,9,78,12,78,9])
print(l2)
print(len(l2))
#create a string list
l3=list(['sai','malli','hema','ganesh'])
print(l3)
#create a heterogenous list
l4=list(["mahi",78,0.9,0,1,(2,3),{0,'a','a'},[89,23,0.11,'sai'],{0:"A",1:'B'}])
print(l4)
lists=l1
#to find the empty list
if len(lists) == 0:
    print("empty list")
else:
    print(len(lists))
#to find index
print(l4[7].index(0.11))
print(l4[5].index(3))
#sum of the list
print(sum(l2))
#7. count the item
print(l2.count(9))
print(l2.count(78))

#8. convert list into set
set1= set([1,2,4,5,6,78,3,4,5])
print(set1)

#9. unique values from list
#converting list into set, set does not duplicate the value

#10. add a item to a heterogenous list
l4[7][2] ='hii'
print(l4)

#11.append a item
l4.append(6000)
print(l4)

#12. insert a item
l3.insert(0,489)
print(l3)
l3.extend([99,1])
print(l3)

#14. deletion
del l3[2]
print(l3)
#15. remove
l4.remove(78)
print(l4)
#16. pop
pop_item=l3.pop(2)
print(pop_item)

#slicing
print(l4[2:5])
print(l2[:7])
print(l2[3:])
print(l2[-6:-1])

#reverse and copy
print(l2)
l2.reverse()
print(l2.copy())

#membership function
print('sai' in l3)
print('kee' in l2)
print("anu" not in l4)

#iteration
for i in l3:
    print(i, end=' ')
print()

#tuple
tup1=tuple(['maldives',0.1,23,1])
print(tup1)
tup_lt=list(tup1)
print(type(tup_lt))
print(tup_lt)
tup=('a','b','c')
tup_str=''.join(tup)
print(tup_str)
tup2=()
#tuple checking
if len(tup2) == 0:
    print("empty tuple")
else:
    print(tup)

#creating tuple from the sublist
tup3=tuple(l2[3:])
print(type(tup3))
print(tup3)

#concatinate 2 tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
print(tuple3[4])
print(tuple3[1],tuple3[-2])
id(tuple3[0])