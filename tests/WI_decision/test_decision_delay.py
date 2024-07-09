import pytest

@pytest.mark.regression
def test_delay():
    """
    TC:T006
    REQ:R005
    
    GIVEN: A working car
    WHEN: When given randomn 100 inputs
    THEN: Output delay should always less than 100ms
    """
    # To do
    delays = [103, 99, 50]
    assert max(delays) < 100
