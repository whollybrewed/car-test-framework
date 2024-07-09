import pytest

def inc(x):
    return x + 1

def test_answer_wrong():
    """
    TC:T001
    REQ:R001
    """
    assert inc(3) == 5

def test_answer_wright():
    """
    TC:T002
    REQ:R001
    """
    assert inc(3) == 4

@pytest.mark.regression
def test_in_regression():
    """
    TC:T003
    REQ:R002
    """
    assert True
