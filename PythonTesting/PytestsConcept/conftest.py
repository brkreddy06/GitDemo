# conftest name is unique, it is used to maintain fixtures methods to available for all the tests
# basically fixture is used to setup the pre requisites of the tests before executing the the tests
import pytest


# @pytest.fixture()   - it will initiate for all the methods which are using it
@pytest.fixture(
    scope="class")  # the scope argument will run before initialising the class, once the methods under class executed then yield statement will print
def setup():
    print("I will be executing first")
    yield  # it is nothing but teardown in TestNG, here in pytest wht ever steps u write under yield those will be executed at last
    print("I will be executed last")


@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ("Ram", "Kumar", "rahulshettyacademy.com")  # Tuple concept using here


@pytest.fixture(params=["chrome", "Firefox", "IE"])  # parameterised fixture
def crossBrowser(request):  # u have to pass request as an argument in the method where as it will return the parameter each time
    return request.param

# if u want to pass multiple values in single run then pass it in () using , as separate
# then system will understand the values provided in the () is consider as single set of data.


@pytest.fixture(params=[("chrome", "Ram", "Kumar"), ("Firefox", "Ram1", "Kumar"), ("IE", "BB")])
def crossBrowser1(request):
    return request.param