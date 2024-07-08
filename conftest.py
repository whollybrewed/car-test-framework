import pytest
import glob

def pytest_collection_modifyitems(items):
    quarantine_list = []
    path = "quarantine*.txt"
    for filename in glob.glob(path):
        with open(filename, 'r') as f:
            quarantine_list = f.read().splitlines()
    if quarantine_list is not None:
        for item in items:
            if item.nodeid in quarantine_list:
                item.add_marker(pytest.mark.quarantine)