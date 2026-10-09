str=input("enter a string")
print(str)
if str.isalpha():
    print("only alpha")
elif str.isdigit():
    print("only digit")
elif str.isalnum():
    print("contains both")
else:
    print("other character")


str="if you think you can or you can't, you are right"
print(str)
print(str.count("you"))
str1="you"
print(str1 in str)
print(str.index("you"))
print(str.find("you"))
print(str.rindex("you"))
print(str.rfind("you"))
print(str.find("python"))
#print(str.index("python"))

str="sarika is good girl"
print(str)
str1=str.replace("good","bad")
print(str1)
print(str.startswith("sarika"))
print(str.startswith("raksh"))
print(str.endswith("girl"))
print(str.endswith("boy"))
