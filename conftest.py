import pytest
import glob
import os

def pytest_deselected(items):
    if not items:
        return
    config = items[0].session.config
    config.deselected = items

def pytest_terminal_summary(terminalreporter, exitstatus, config):
    reports = terminalreporter.getreports('')
    content = os.linesep.join(text for report in reports for secname, text in report.sections)
    deselected = getattr(config, "deselected", [])
    if deselected:
        terminalreporter.ensure_newline()
        terminalreporter.section('Deselected tests', sep='-', yellow=True, bold=True)
        content = os.linesep.join(item.nodeid for item in deselected)
        terminalreporter.line(content)

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