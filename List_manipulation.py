#lists
l1=[[40,50,78,90,99,89],[45,90,87,78,23,67],[67,89,90,12,78,67],[91,61,92,54,71,32]]
r=len(l1)
print(r)
print(max(l1[0]))
print(min(l1[3]))
d=sum(l1[0])
print(d)
avg1 = (sum(l1[0])/len(l1[0]))
avg2 = (sum(l1[1])/len(l1[1]))
avg3 = (sum(l1[2])/len(l1[2]))
avg4 = (sum(l1[3])/len(l1[3]))
print(avg1, avg2, avg3, avg4)
l2=list([avg1,avg2,avg3,avg4])
print(l2)
print(type(l2))
print(max(l2))
print(min(l2))
print(l1[3][-1])
print(l2)


list1 = [1,2,3,4,5,67,0.9,0,1,'sai','s']
#access value
#access the value by index
list1[0]=90
print(list1)

#append() adds a new element to the list
list1.append('hey')
print(list1)

#extend() used to connect two lists
list1.extend(['h',25,0.01])
print(list1)

#insert() helps to insert the value in the mentioned index
list1.insert(4,89)
print(list1)

#count() shows the number of times the elements repeated (duplicate elements)
x=list1.count(1)
print(x)

#pop() used to remove the element in given index
list1.pop(4)
print(list1)

#this removes the last element in the list
list1.pop()
print(list1)

#remove the element or remove the very first element (duplicate element)
list1.remove(1)
print(list1)

#len() gives the number of elements in the list
print(len(list1))

#sum() gives the sum of the values in the list
print(sum(list1[:2]))

#min() gives the minimum value in the list
print(min(list1[0:4]))

#max() gives the maximum value in the list
print(max(list1[0:5]))

#reverse() the reverse the indexing
list1.reverse()
print(list1)

#copy() copy the list one more time
list2=list1.copy()
print(list2)

#sort() helps for elements for sorting where sorting not helps in strings
y=list('1345789')
print(y)

#clear() clears the list
list1.clear()
print(list1)

#slicing
list1=[1,2,3,6,7,9,80,87]
print(list1)

print(list1[0:5])
print(list1[:4])
print(list1[0:])
print(list1[2:4])
print(list1[0])
print(list1[:])





