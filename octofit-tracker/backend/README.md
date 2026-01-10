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


## Example API Root Response (Codespaces)


When running in GitHub Codespaces, the API root returns URLs like:

```
{
	"users": "https://YOUR_CODESPACE_NAME-8000.app.github.dev/api/users/",
	"teams": "https://YOUR_CODESPACE_NAME-8000.app.github.dev/api/teams/",
	"activities": "https://YOUR_CODESPACE_NAME-8000.app.github.dev/api/activities/",
	"leaderboards": "https://YOUR_CODESPACE_NAME-8000.app.github.dev/api/leaderboards/",
	"workouts": "https://YOUR_CODESPACE_NAME-8000.app.github.dev/api/workouts/"
}
```

Replace `YOUR_CODESPACE_NAME` with your actual Codespace name. The key strings `-8000.app.github.dev/api/users` and `-8000.app.github.dev/api/workouts` will always appear in the respective URLs.

Notes:
- Use Django's ORM for database creation and operations (do not run direct MongoDB scripts to create models/data).
- Check `.github/instructions/octofit_tracker_setup_project.instructions.md` for project-specific guidelines.
