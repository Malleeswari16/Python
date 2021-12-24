#defining the dictionary using the {}
dic1={"JS":"ATOM","CS":"VS","Python":"[pycharm,sublime]",'Java':"{'JSE':'Netbrains','JEE':'Eclipse'}"}

# items() gives the value of the every element with the key in tuple
print(dic1.items())

# values() gives the elements
print(dic1.values())

# keys() gives the key values
print(dic1.keys())

# accessing using the key value
print(dic1['Java'])
print(dic1['Python'])

# len() gives the number of key values
print(len(dic1))

# copy() just the same dictionary
print(dic1.copy())

# get() fetch the element with the key value given
print(dic1.get("CS"))

# creating and  changing using the assignment
dic1['CS']='Comp'
print(dic1)
dic1['hii']='world'
print(dic1)

# popitem() uses to delete the
print(dic1.popitem())
print(dic1)

# pop() use to delete the particular key and their elements
print(dic1.pop("CS"))
print(dic1)

#deletion
del dic1['Python']
print(dic1)

# clear() deletes everything in dictionary
dic1.clear()
print(dic1)

