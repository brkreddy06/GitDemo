# Strings performs more likely as List
# To check the substring validation in the main string then use "in" command
# + is used to do concatenation
# split() method is used to split the string
# strip() - to removes the white spaces before & after in a string
# lstrip() - to remove left side white space in a string
# rstrip() - to remove right side white space in a string


str = "RamkumarAcademy.com"
str1 = "Reddy"
str2 = "ram"
print(str[0])  # to print first letter R in the string
print(str[3:8])  # it prints kumar
print(str[-1])  # prints last letter m

print(str + str1)  # concatenation

var = str.split(".")  # split is a command to split the string
print(var)
print(var[0])

print(str2 in str)  # to check the string2 value is present in string1. Substring check

str3 = " Welcome "
print(str3.strip())  # it removes the spaces from both start and end
print(str3.lstrip())  # it removes lest side space
print(str3.rstrip())  # it removes right side space
