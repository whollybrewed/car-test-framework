import pytest
import glob

qlist = []
def pytest_collection_modifyitems(items):
    path = "quarantine*.txt"
    for filename in glob.glob(path):
        with open(filename, 'r') as f:
            qlist = f.read().splitlines()

    for item in items:
        if item.nodeid in qlist:
            item.add_marker(pytest.mark.quarantine)