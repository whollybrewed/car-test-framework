import pytest

def test_access_auth_ask():
    """
    TC:T007
    REQ:R006
    
    GIVEN: A steering wheel and brake in operation
    WHEN: A control command is sent
    THEN: The system requests authentication
    """
    # To do
    auth_request = True
    assert auth_request

def test_bad_auth():
    """
    TC:T008
    REQ:R006
    
    GIVEN: The system requests authentication
    WHEN: An invalid ID is sent
    THEN: The system denies access
    """
    # To do
    access_denied = True
    assert access_denied

def test_bad_auth():
    """
    TC:T009
    REQ:R007
    
    GIVEN: A steering wheel and brake in operation
    WHEN: User manually gain control
    THEN: The system should handover the control
    """
    # To do
    manual_mode = True
    assert manual_mode
