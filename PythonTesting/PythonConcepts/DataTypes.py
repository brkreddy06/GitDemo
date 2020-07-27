# Data type - List (array) The list is a versatile data type exclusive in Python. In a sense, it is the same as the
# array in C/C++. But the interesting thing about the list in Python is it can simultaneously hold different types of
# data. Formally list is an ordered sequence of some data written using square brackets([]) and commas(,).
values = [1, 2, "ram", 4, 5.5, 6.6]

print(values[0])  # 1
print(values[2])  # ram
print(values[-1])  # it will print last one 6.6 (6-1 = 5) 5th one will consider
print(values[1:4])  # it prints 2,ram,4 and not 4th one i.e 5.5, because it considers 1,2,& 4-1=3 index(: called 'east to')

# if u wanna insert in between the array then use insert command
values.insert(3, "kumar")  # inserting the value after 3rd index number
print(values)  # the output is [1, 2, 'ram', 'kumar', 4, 5.5, 6.6]

values.append("End")  # append command will add the last index+1 place
print(values)  # [1, 2, 'ram', 'kumar', 4, 5.5, 6.6, 'End']

values[2] = "Ram" # update the index value
del values[0]  # delete the index value
print(values)  # [2, 'Ram', 'kumar', 4, 5.5, 6.6, 'End']

# Tuple - Same as LIST data type but it is immutable (immutable means not able to update, modify and it is protected)
# Tuple is another data type which is a sequence of data similar to list. But it is immutable. That means data in a
# tuple is write protected. Data in a tuple is written using parenthesis and commas

val = (1, 2, "ram", 4, 5.8)
print(val[0])  # 1
# val.insert(3, "kumar") - insert command not applicable
# val.append("end")  - append command not applicable
# del val[0] - del command not applicable

# val[2] = "Ram" - update command not applicable
# print(val)  # it gives error because it won't support item assignment like List

# Dictionary - Python Dictionary is an unordered sequence of data of key-value pair form. It is similar to the hash
# table type. Dictionaries are written within curly braces in the form key:value. It is very useful to retrieve data
# in an optimized way among a large amount of data

dic = {"a":3, "b":567, "c":"Welcome to Python world", 6:"a"+"b"}
print(dic)
print(dic["a"])
print(dic["b"])
print(dic["c"])
print(dic["a"], dic[6])
print(dic[6])

# How to create Dictionaries at run time and add data into it
dict = {}
dict[1] = 35
dict["first name"] = "Ramkumar"
dict["last name"] = "Reddy"
dict["gendar"] = "male"
print(dict)
print(dict["first name"], dict["last name"], dict["gendar"], dict[1])