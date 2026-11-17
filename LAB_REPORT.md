# Lab 10 — CI/CD Pipeline Report

**Student:** Reem Saab

## Implementation

The Python application returns a personalized greeting. Three tests check two inputs and the greeting printed by the command-line entry point. The Jenkins pipeline selects the appropriate shell and virtual environment path for Windows or Unix-like agents.

1. **Setup:** Create a virtual environment and install project dependencies.
2. **Lint:** Check application, deployment script, and tests with flake8.
3. **Test:** Run pytest unit tests.
4. **Coverage:** Generate terminal and XML coverage reports using coverage.py; enforce a 90% coverage threshold.
5. **Security Scan:** Run Bandit against the application and deployment script.
6. **Deploy:** Copy `app.py` to a local deployment folder and run the copied script.

The pipeline archives the generated coverage XML file and deployed application, then cleans the workspace after the build.

## Build verification

**`Python-CI-CD` build #1 finished with `SUCCESS` on November 17, 2026.** Jenkins 2.580.2 ran the pipeline on Windows with Python 3.10.11. The job loaded `Jenkinsfile_Reem_Saab` from GitHub branch `main` at commit [`fa4630e`](https://github.com/reemrsaab/jenkins_project/commit/fa4630e8dd3e1da9cce2531fb5dedb1d7f77e933).

| Stage | Result |
| --- | --- |
| Setup | Created the virtual environment and installed all dependencies. |
| Lint | flake8 passed for the application, deployment script, and tests. |
| Test | All three pytest tests passed. |
| Coverage | All four statements in `app.py` ran, giving 100% coverage. Jenkins archived `coverage.xml`. |
| Security Scan | Bandit reported zero findings in `app.py` and `deploy.py`. |
| Deploy | The deployed `app.py` ran successfully and Jenkins archived it. |

## Jenkins console excerpt

```text
3 passed in 0.03s
app.py       4      0   100%
Wrote XML report to coverage.xml
No issues identified.
Hello, World from Reem Saab!
[WS-CLEANUP] done
Finished: SUCCESS
```
