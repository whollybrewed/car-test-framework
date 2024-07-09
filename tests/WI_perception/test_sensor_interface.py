import pytest

def test_port_access():
    """
    TC:T001
    REQ:R001
    
    GIVEN: A port with locked permission  
    WHEN: User attempt access
    THEN: Sensor should deny it 
    """
    # To do
    sensor_deny_message = True
    assert sensor_deny_message


@pytest.mark.regression
def test_port_scan():
    """
    TC:T002
    REQ:R001

    GIVEN: An interface 
    WHEN: User initiate random scanning
    THEN: The interface ID should not be reveal
    """
    # To do
    scan_result_empty = True
    assert scan_result_empty