from OopsConcept import Calculator


class childImpl(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 5, 7)

    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()


obj = childImpl()
print(obj.getCompleteData())
print(obj.num2)