
# assert method - always uses the condition, in any case condition fails then it will break the test
# raise & Exception are keywords used to show the exception if condition not mats
# pass keyword used to process the line without breaking
# finally keyword is connected with try & except, this will be used when you use try & except mechanism. It will execute whether exception triggers or not

ItemsInCart = 0

#2 items will be added to cart

if ItemsInCart != 2:
    #raise Exception("Product carts not matching")
    pass
#assert (ItemsInCart == 2) # if the condition fails it will show AssertionError, if passes then it won't show
assert (ItemsInCart == 0)

#try, catch (except keyword is used in python for catch)

#here in try except block we are printing the customised exception message
try:
    with open('filelog.txt', 'r') as reader:
        reader.read()

except:
    print("some how I reached this block because there is a failure in try block")

#here python will print the exception message, we can know that wht is the exact problem is
try:
    with open('filelog.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print("cleaning up the resources")