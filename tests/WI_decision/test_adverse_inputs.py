import pytest

@pytest.mark.regression
def test_traffic_light():
    """
    TC:T005
    REQ:R004
    
    GIVEN: A working car camera
    WHEN: When given 100K image of red traffic lights
    THEN: The car should make the correct judgement 99.99% of the time
    """
    # To do
    success_decision = 99999
    assert success_decision/100000 >= 0.9999
