# OctoFit Tracker — Backend

## Setup (local development)

Create the Python virtual environment:

```bash
python3 -m venv octofit-tracker/backend/venv
```

Activate and install requirements:

```bash
source octofit-tracker/backend/venv/bin/activate
pip install -r octofit-tracker/backend/requirements.txt
```

Notes:
- Use Django's ORM for database creation and operations (do not run direct MongoDB scripts to create models/data).
- Check `.github/instructions/octofit_tracker_setup_project.instructions.md` for project-specific guidelines.
