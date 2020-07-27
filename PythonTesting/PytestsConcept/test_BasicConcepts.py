# Any pytest file should start with test_ or end with _test
# whatever code you are going to write in pytest it has to be in function
# Pytest methods names should start with test
# Any code should be wrapped in methods only
# Each method considers as a separate test case in Pytest
# Same method name should not have in Pytest if there is a same method then it overrides
# -k stands for method name execution, -s logs in output, -v stands for more info metadata
# You can mark (tag) tests @pytest.mark.smoke and then run with -m
# You can skip a test using @pytest.mark.skip
# @pytest.mark.xfail - not show the status of the test case in the report
# Fixtures are used as setup and tear down methods for test cases.
# conftest file to generalize fixture and make it available to all test cases
# Datadriven and parametrisation can be done with return statements in Tuple format
# Scope - When you define fixture scope to class only, it will run once before the class is initiated and at the end after all class methods are executed

import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    print("Hello Pytest")


def test_GreetCreditCard(setup): # here calling the fixtures which is available in conftest file by passing setup argument
    print("Good morning")


def test_CrossBrowser(crossBrowser):
    print(crossBrowser)


def test_CrossBrowser1(crossBrowser1):
    #print(crossBrowser1)
    print(crossBrowser1[1])