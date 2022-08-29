import re

str = input('please provide first number: ')
str2 = input('please provide second number: ')
print(str,'+',str2,'=',int(str)+int(str2))

if re.match("[1-7]"