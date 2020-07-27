import pytest


@pytest.mark.usefixtures("dataLoad")
class TestExample2:

    def test_editProfile(self, dataLoad):  # if you returning some data then fixture method should pass in class method argument
        print(dataLoad)  # if you want to print the data which is available in fixture then u have to pass that argument into class method
        print(dataLoad[0]) # if you want to print data separately then use index
        print(dataLoad[1])
        print(dataLoad[2])


