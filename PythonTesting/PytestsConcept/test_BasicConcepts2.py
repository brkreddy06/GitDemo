import pytest


@pytest.mark.smoke
def test_messagePrint():
    msg = "Hello"
    assert msg == "Hi", "Test failed because string does not match"

@pytest.mark.xfail
def test_SecondCreditCard(setup):  # here calling the fixtures which is available in conftest file by passing setup argument
    a = 4
    b = 6
    assert a + 2 == b, "Addition does not match"


