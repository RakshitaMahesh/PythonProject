# using in

str=input("enter a string")
str1=""
for i in str:
    if i in str1:
        pass
    else:
        str1=str1+i
print(str1)

# using not in

str=input("enter a string")
str1=""
for i in str:
    if i not in str1:
        str1=str1+i
    else:
        pass
print(str1)


