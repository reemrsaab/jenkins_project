# Lab 10 — Jenkins CI/CD Pipeline

**Student:** Reem Saab  
**Course:** Software Tools Lab — Fall 2026–2027

This Python project demonstrates Jenkins-based CI/CD using six stages: Setup, Lint, Test, Coverage, Security Scan, and Deploy.

## Files
- `app.py` — greeting application
- `tests/test_app.py` — unit tests
- `requirements.txt` — CI dependencies
- `Jenkinsfile_Reem_Saab` — Jenkins declarative pipeline
- `deploy.py` — local deployment script
- `LAB_REPORT.md` — implementation notes and verification

## Jenkins setup
1. Install Jenkins with Git, Pipeline, SSH Agent, and Workspace Cleanup plugins. Put Python 3 with `venv` on the Jenkins agent's `PATH`.
2. Create a Pipeline job named `Python-CI-CD`.
3. Select **Pipeline script from SCM**, choose **Git**, and enter the repository URL.
4. Set the branch to `*/main` and the **Script Path** to `Jenkinsfile_Reem_Saab`.
5. Run **Build Now** and inspect Console Output and archived artifacts.

The pipeline uses `python` on Windows and `python3` on Unix-like agents. After deployment, Jenkins archives `deployment/app.py` and `coverage.xml` before cleaning the workspace.

## Local verification
```bash
python3 -m venv venv
venv/bin/python -m pip install -r requirements.txt
venv/bin/python -m flake8 app.py deploy.py tests
venv/bin/python -m pytest -q tests
venv/bin/python -m coverage run --source=app -m pytest -q tests
venv/bin/python -m coverage report -m --fail-under=90
venv/bin/python -m bandit app.py deploy.py
venv/bin/python deploy.py --destination deployment
venv/bin/python deployment/app.py
```
