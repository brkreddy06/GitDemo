import pytest

from PytestsConcept.BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):  # inheriting from BaseClass to utilise methods & variables of the BaseClass

    def test_editProfile(self, dataLoad):  # if you returning some data then fixture method should pass in class method argument
        print(dataLoad[0])
        print(dataLoad[1])
        log = self.getLogger()  #Utilising the BaseClass methods to print the logs. what ever statements using in log that only prints in log report or html report
        log.info(dataLoad[0])
        log.info(dataLoad[1])

