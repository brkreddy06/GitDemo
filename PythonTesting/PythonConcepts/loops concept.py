# if else
greetings = "Good Morning"
a = 4

# if greetings == "Morning":
if a >= 2:
    print("condition is matched")
    print("second line")

else:
    print("condition is not matched")

print("the code is completed")

# for loop
print("-------for loop--------------------")
obj = [2, 3, 4, 5, 6]
for i in obj:
    # print(i) # it iterate and print all the values
    # name = "{} {}".format("multiple of", i)
    # print(name, i * 2)  # it print multiples of 2 ex: 2*2=4, 3*2=6, 4*2=8 etc
    print("Multiple of", i, "*", i, "=", i * 2)

# Sum of first five natural numbers 1+2+3+4+5 = 15
# range(i, j) -> i to j-1
print("-------------- natural number---------------")
summation = 0
for j in range(1, 6):
    print("j value", "=", j)
    print("Summation value", "=", summation)
    print("New Summation value:", summation, "+", j, "=", j + summation)
    summation = summation + j

print("Addition of natural numbers", summation)

print("**********************************************************************")
# if you give the 3rd index in 'range' then it will skip the iteration of 2. ex: 1st iteration it prints 1,
# 2nd iteration it prints 1+2 =3, 3rd iteration 3+2 =5, and so on till 10-1

for k in range(1, 10, 2):  # prints 1,3,5,7,9
    print(k)

print("**************************Next loop************************************")
# if you provide single index in 'range' by default the python considers as zero index and prints rest of the numbers

for l in range(10):  # prints 0 to 9
    print(l)
