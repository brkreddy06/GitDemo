
#refer conftest for fixture syntax
import pytest


#def test_fixtureDemo(setup):  # providing the connection to the fixture by passing fixture method into firtDemo method
 #   print("I will be execute steps in fixtureDemo method")

@pytest.mark.usefixtures("setup")   # the fixture is applicable for all the methods present under class. This is for using the fixture globally
class TestExample():

    def test_fixtureDemo1(self):
        print("I will be execute steps in fixtureDemo1 method")

    def test_fixtureDemo2(self):
        print("I will be execute steps in fixtureDemo2 method")

    def test_fixtureDemo3(self):
        print("I will be execute steps in fixtureDemo3 method")