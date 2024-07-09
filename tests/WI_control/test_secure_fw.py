import pytest

def test_secure_update():
    """
    TC:T010
    REQ:R008
    
    GIVEN: A new firmware
    WHEN: User performs install 
    THEN: memory is encrypted and the integrity of the critical files are checked 
    """
    # To do
    mem_encrypted = True
    check_integrity = True
    assert (mem_encrypted and check_integrity)

def test_downgrade():
    """
    TC:T011
    REQ:R009
    
    GIVEN: An older version firmware
    WHEN: User trys to install
    THEN: The system denies installation
    """
    # To do
    install_denied = True
    assert install_denied

