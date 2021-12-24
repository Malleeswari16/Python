#strings
str = "This is the Python program for Strings"
str1 = "hello123"
str2 = "  "
str3 = "abcdef"

#length()
print(len(str))

#count()
print(str.count('is',0,len(str)))

#ialpha(),#isalnum,#isspace()
print("The given string(str) is only a alphabet-->",str.isalpha())
print("The given string(str1) is only a alphabet-->",str1.isalnum())
print("The given string(str2) is only a alphabet-->",str2.isspace())
print("The given string(str3) is only a alphabet-->",str3.isalpha())

#join
l=['im','a','python','programmer']
a='_'
print(a.join(l))
print(str2.join(str1))
print(str2.join(str))

#find and rfind
a="This is my Python assignment of Strings"
print(a.find('is',0,len(a)))
print(a.rfind('is',0,len(a)))

#startswith() and endswith()
b='my father is my inspiration.'
c='my'
if b.startswith(c):
    print('yes')
elif b.endswith(c):
    print("yes")
else:
    print("no")

#isupper() and islower()
c="TUTORIALFORPYHTON"
print("islowercase:",b.islower())
print("isuppercase",c.isupper())

#lower(),upper(),title(),swapcase()
print("The string a is completely with lower case: " ,a.lower())
print("The string a is completely with upper case: " ,a.upper())
print("The string a is completely with title case: " ,a.title())
print("The string a is completely with swap case: "  ,a.swapcase())

#strip(),lstrip(),rstrip()
H="---This is the technology world---"
print(H.strip('-'))
print(H.rstrip('-'))
print(H.lstrip('-'))

#min() and max()
d="geeksforgeeks"
print("prints the most repeated letter",max(d))
print("prints the less repeated letter",min(d))

#translate()
str1='mit'
str2='ljy'
map=str.maketrans(str1,str2)
print(b.translate(map))


#default order
String1 = "{} {} {}".format('Geeks', 'For', 'Life')
print(String1)

# Positional Formatting
String1 = "{1} {0} {2}".format('Geeks', 'For', 'Life')
print(String1)

# Keyword Formatting
String1 = "{l} {f} {g}".format(g='Geeks', f='For', l='Life')
print(String1)

#slicing
print(b[0:])
print(b[0:3])

#escaping
print('C:\\path\\apps\\pythonfiles')
print('''I'm a "coder"''')
print('I\'m a coder')



