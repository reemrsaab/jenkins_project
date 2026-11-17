# Lab 10 — CI/CD Pipeline Report

**Student:** Reem Saab

## Implementation

The Python greeting application returns a personalized greeting. Its unit tests verify expected behavior for two inputs. The Jenkins declarative pipeline runs the following stages:

1. **Setup:** Create a virtual environment and install project dependencies.
2. **Lint:** Check application, deployment script, and tests with flake8.
3. **Test:** Run pytest unit tests.
4. **Coverage:** Generate terminal and XML coverage reports using coverage.py; enforce a 90% coverage threshold.
5. **Security Scan:** Run Bandit against the application and deployment script.
6. **Deploy:** Copy `app.py` to a local deployment folder, verify that the file exists, and execute it.

The pipeline archives the generated coverage XML file and deployed application, then cleans the workspace after the build.

## Build verification

A Jenkins build must be executed on a configured Jenkins agent to verify end-to-end CI/CD. Record the Jenkins build number, stage results, and console output after running the job. Do not interpret local Python checks as a successful Jenkins build.

| Stage | Result |
| --- | --- |
| Setup | Awaiting Jenkins execution |
| Lint | Awaiting Jenkins execution |
| Test | Awaiting Jenkins execution |
| Coverage | Awaiting Jenkins execution |
| Security Scan | Awaiting Jenkins execution |
| Deploy | Awaiting Jenkins execution |

## Notes

A Linux/Unix Jenkins agent, Python 3, Jenkins Git/Pipeline plugins, and the Workspace Cleanup plugin are required. The Jenkins job's Script Path must match `Jenkinsfile_Reem_Saab`.

## Local checks performed

- Python `unittest`: **2 tests passed**.
- `compileall`: **passed**.
- Local deployment script: **passed**; the copied application printed `Hello, World from Reem Saab!`.
- Lint, coverage, Bandit, and the actual Jenkins build have **not yet been verified** in this environment.
