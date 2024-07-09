import pytest

def test_sensor_encrypt():
    """
    TC:T003
    REQ:R002
    
    GIVEN: A sensor sends a signal  
    WHEN: The signal is captured
    THEN: signal should only be decrypted by the correct key
    """
    # To do
    signal_encrypted = True
    siganl_decrypt_success = True
    assert (signal_encrypted and siganl_decrypt_success)
