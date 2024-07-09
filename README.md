## Test Framework
This demo test framework is constituted of three components:
- [**Pipeline**](.github/workflows/master_pipe.yml): Defines the schedule and the scope of each test stage.
- [**Traceability Management**](trace_manager.py): An automation tool that updates and maintains the requirement traceability matrix (RTM).
- **Test runner**: pytest [config](conftest.py) and [test cases]((/tests)) 

```
┌──────────────────────────────┐                                                
│   Pipeline                   │                                                
│   Stage 1: Smoke test        │                 ┌─────────────────────────────┐
│   Stage 2: Acceptance test   │                 │                             │
│   Stage 3: Regression test   │                 │   Traceability Management   │
│   Stage 0: Quarantine        │                 │  -Requirement ID            │
└───────────────────┬───▲──────┘                 │  -Test case ID              │
                    │   │                        │  -Test report               │
                    │   │                        │                             │
                    │   │                        └───────┬───┬─────────────────┘
                    │   │                                │   │                  
                 ┌──▼───┴─────────┐                      │   │                  
                 │                ◄──────────────────────┘   │                  
                 │  Test runner   │                          │                  
                 │                ◄──────────────────────────┘                  
                 └────────────────┘                                             
```
The following logics apply:

- All submission triggers stage 1
- Pass in stage 1 triggers stage 2
- Pass in stage 2 triggers stage 3
- Fail in any stage triggers stage 0

The followings are considered business decisions, thus require human inputs:
- Adding tests to stage 3
- Removing tests from stage 0

### Report Matrix 
A test report will be generated every time all stages have been performed. The report can be found as an artifact of job `Generate final report` under `Actions` -> `Master test pipeline`  
