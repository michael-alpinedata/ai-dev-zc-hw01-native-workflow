## Commands

- `uv sync` - install dependencies
- `uv run python manage.py test` - run the whole test suite
- `uv run python manage.py test chores.tests` - run the chores test module

## Rules

- Dependencies are added in `pyproject.toml`. Do not add one without
  asking

## Documents

- `_docs/process.md` - how work is organized
- `_docs/tasks.md` - index of the canonical GitHub task issues
- `_docs/plan.md` - product specification
- Before writing tests, read `_docs/testing-guidelines.md`
- For anything touching the UI, read `_docs/design-system.md`