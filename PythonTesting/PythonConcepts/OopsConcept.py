# Class is a user defined protocol / prototype
# Constructor is one method which is automatically called when you create object for any class. Default Constructor will be present.
# self keyword is mandatory for calling variable names into method
# instance and class variables have whole different purpose, one is attached to the object and another one is not attached to object.
# constructor name should be __init__
# new keyword is not required when you create the object for a class
# Inheritance is nothing but acquiring properties of parent class


class Calculator:
    num = 100  # class variable

    def __init__(self, a, b):  # parameterised constructor syntax
        self.firstNumber = a  # firstNumber & secondNumber are instance variable, self is an object
        self.secondNumber = b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing as method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + self.num  # or you can declare as class name eg: Calculator.num, this is applicable only for class variable


obj = Calculator(5, 7)  # syntax to create a object for the class in Python
obj.getData()
print(obj.Summation())

obj1 = Calculator(6, 8)
obj1.getData()
print(obj1.Summation())