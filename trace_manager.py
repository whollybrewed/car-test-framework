import glob
import ast
import csv
from dataclasses import dataclass, field
from typing import List
from tabulate import tabulate

MAX_STAGE = 3

#################################
# helper functions
#################################
def file2list(file_path):
    try:
        with open(file_path, 'r') as f:
            lines = f.read().splitlines() 
        return lines
    except FileNotFoundError:
        return None


def init_obj(file_path):
    req_objs = []
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            req_obj = ReqObject(id=row['id'],
                                description=row['description'],
                                risk=row['risk'])
            req_objs.append(req_obj)
    return req_objs


def generate_report(req_objs):
    report_data = []
    req_titles = []
    for req_obj in req_objs:
        table_data = []
        tcs = req_obj.tcs
        for tc in tcs:
            table_data.append([tc['tcid'],
                               tc['nodeid'],
                               tc['stage1'],
                               tc['stage2'],
                               tc['stage3']])
        report_data.append(table_data)
        header = ["TCID", "Test Name", "Stage 1", "Stage 2", "Stage 3"]
        req_titles += [f"[{req_obj.id}]: {req_obj.description}\nRisk: {req_obj.risk}\n"]
    final_table = ""
    for i in range(len(report_data)):
        # final_table += f"<br><strong>{req_titles[i]}</strong>"
        final_table += req_titles[i]
        # table = tabulate(report_data[i], headers=header, tablefmt="html")
        table = tabulate(report_data[i], headers=header, tablefmt="pretty")
        final_table += table
        final_table += "\n\n"
    with open("report.txt", "w") as f:
        f.write(final_table)

#################################
# Requirement matrix builder
#################################
@dataclass
class ReqObject:
    id: str
    description: str
    risk: str
    tcs: List[dict] = field(default_factory=list)

    def build_trace(self):
        file_list = glob.glob('tests/**/*.py', recursive=True)
        for file_path in file_list:
            with open(file_path, "r") as source:
                tree = ast.parse(source.read())
            for node in tree.body:
                if isinstance(node, ast.FunctionDef) and "test" in node.name:
                    docstring = ast.get_docstring(node)
                    nodeid = f"{file_path}::{node.name}"
                    tcid, reqid = self.extract_doc(str(docstring))
                    if reqid == self.id:
                        tc_state = {'tcid': tcid,
                                    'nodeid': nodeid,
                                    'stage1': 'Not tested',
                                    'stage2': 'Not tested',
                                    'stage3': 'Not tested'}
                        self.tcs.append(dict(tc_state))
        return False if self.tcs is None else True

    def track_test_progress(self):
        for tc in self.tcs:
            for stage_num in range(1, MAX_STAGE+1):
                quarantine_list = file2list(f"quarantine{stage_num}.txt")
                pass_list = quarantine_list = file2list(f"pass{stage_num}.txt")
                if quarantine_list is not None:
                    if tc['nodeid'] in quarantine_list:
                        tc[f'stage{stage_num}'] = 'Quarantined'
                if pass_list is not None:
                    if tc['nodeid'] in pass_list:
                        tc[f'stage{stage_num}'] = 'Passed'

    @staticmethod
    def extract_doc(s):
        parts = s.split()
        tc_prefix = "TC:"
        req_prefix = "REQ:"
        tc_id = [part[len(tc_prefix):] for part in parts if part.startswith(tc_prefix)]
        req_id = [part[len(req_prefix):] for part in parts if part.startswith(req_prefix)]
        return tc_id[0] if tc_id else None, req_id[0] if req_id else None


#################################
# Main
#################################
if __name__ == '__main__':
    req_path = "requirement_table.csv"
    req_objs = init_obj(req_path)
    for req_obj in req_objs:
        trace_exists = req_obj.build_trace()
        if trace_exists:
            req_obj.track_test_progress()
    generate_report(req_objs)
