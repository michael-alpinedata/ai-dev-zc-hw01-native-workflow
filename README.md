# Family Chore Management

Django project for managing shared household chores.

## Setup

Install [uv](https://docs.astral.sh/uv/), then run:

```powershell
uv sync
uv run python manage.py migrate
uv run python manage.py runserver
```

The Django project configuration is in `config/`, and the `chores` app is
registered in `config/settings.py`.

## Project documents

- [Product specification](./_docs/plan.md)
- [Task issue index](./_docs/tasks.md) — GitHub Issues are the canonical backlog.
- [Work process](./_docs/process.md)