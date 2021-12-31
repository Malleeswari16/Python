#string
#1. create string using "" and ''

a="Welcome to the pycharm community \n"
b='                  ~~Jet Brains'
print(a,b)

#2.create a list of Character from list.
l=['P','y','t','h','o','n']
for i in l:
    print(i ,"\n")

#3.create a string from first 3 letters and last 3 letters.
c="palindrome"
print(c[0:3]+c[7:10])

#4.print in lower and upper case
str1=input("enter the string:")
print(str1.lower())
print(str1.upper())

#5.removing the white space
str2=input("give the string here:")
print(str2.replace(" ",""))

#6.remove the white space from right
str3=input("enter the string here:")
print(str3.rstrip())

#7. justification
str4=input()
x=str4.center(60," ")
print(x)

#8.take multiple lines
A=''' pycharm is one the best idle used by many of the students and the working professionals which is very portable and easy to use
                                                                                                                            ~~Jet Brains'''
print(A)

#9.split the lines
y="A rose is a woody\nperennial\nflowering plant of the genus Rosa\nfamily Rosaceae\ror the flower."
print(y.splitlines())

#12. partition
m=input("enter the string:")
print(m.partition('python'))
print(m.partition("is"))

n="python is very easy to learn"
p="programming"
if "python" in n:
    print("python {}".format(p))

# 14.concatenate the two user inputs.
str1 = input("enter the first string:")
 str2 = input("enter the second string:")
print(str1 + str2)
print("{} {}".format(str1, str2))

#15.multiply the string
h="hii!!!"
print(h*3)