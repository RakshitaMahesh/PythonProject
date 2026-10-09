# reversing a string

str=input("enter a string")
rev="  "
for i in str:
    rev=i+rev
print(rev)

#reversing a sentence

str=input("enter a sentence")
str1=str.split()
print(str)
print(str1)
rev=""
for i in str1:
     rev=i+" "+rev
print(rev)

#palindrome

str=input("enter a string")
rev=""
for i in str:
    rev=i+rev
print(rev)
if str==rev:
    print("palindrome")
else:
    print("not palindrome")



