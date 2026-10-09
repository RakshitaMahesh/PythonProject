# removing spaces from 1st and last
str="  chandru is drinking  "
print(str)
str1=str.lstrip() # removes starting space
print(str1)
str2=str.rstrip() # removes last spcae
print(str2)
str3=str.strip()  #removes both the spaces
print(str3)


str=input("enter a string")
print(str)
str1=""
for i in str:
    if i==" ":
        pass
    else:
        str1=str1+i
print(str1)

str="Ramya"  #packing
print(str)
r1,r2,r3,r4,r5=str  #unpacking
print(r1)
print(r2)
print(r3)
print(r4)
print(r5)

alpha=input("enter a alpha")
ascii=ord(alpha)
print(ascii)


ascii=int(input("enter a ascii value"))
alpha=chr(ascii)
print(alpha)