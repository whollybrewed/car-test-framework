import pytest
import glob

quarantine_list = []
def pytest_collection_modifyitems(items):
    path = "quarantine*.txt"
    for filename in glob.glob(path):
        with open(filename, 'r') as f:
            quarantine_list = f.read().splitlines()

    for item in items:
        if item.nodeid in quarantine_list:
            item.add_marker(pytest.mark.quarantine)