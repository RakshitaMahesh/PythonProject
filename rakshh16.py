#string interning

str1="raksh"
str2="raksh"
str3="m"
str4="m"
str5="mahesh"
print(id(str1))
print(id(str2))
print(id(str3))
print(id(str4))
print(id(str5))

#string formatting

name=input("enter a name")
print('hi {}'.format(name))

