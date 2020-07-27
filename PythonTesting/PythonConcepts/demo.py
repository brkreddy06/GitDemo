print("hello")

# first code of line
a = 10
b, c, ram = 6, 5.0, "ramkumar"
d = a+b+c
E = d+10.6

print(a)
print(b)
print(c)
print(d)
print(ram)
print(E)

# print("the value is" + b) - it won't work as python not concatenate both string and variable

con = "{} {} {}".format("the value is", b, ram)
# print("{} {} {}".format("the value is", b, ram))
# print("the value is", b, ram)
print(con)
print(a+b+c+d)
# print(a+b+c+d+ram) - can not concatenate different variables, format command needs to be used for different
# variable concatenation

print(a, b, c, d)
print(type(a), type(b), type(c), type(ram))

c = 100+3j  # complex - numeric data type
print("The type of variable having value", c, " is ", type(c))
a=100
print("The type of variable having value", a, " is ", type(a))