# Qr Dashboard

To run cookie cutter, use this command:

```bash
cookiecutter ./cookiecutter-django-template
```

## Docker compose

To run with docker compose, run this:

```bash
docker-compose down -v
docker-compose up
```

The first command is so that we can remove dangling container and volumes, from previous docker runs.

## Pre commit

Check install:

```bash
pre-commit --version
```

Install if missing:

```bash
pip install pre-commit
```

Once installed, run this:

```bash
pre-commit install
```

Execute pre-commit:

```bash
pre-commit run --all-files
```

If we get an error like this:

```bash
==> File /Users/jesuscaballerorodriguez/.cache/pre-commit/repoqeelck9u/.pre-commit-hooks.yaml
==> At Hook(id='docformatter-venv')
==> At key: language
=====> Expected one of conda, coursier, dart, docker, docker_image, dotnet, fail, golang, haskell, julia, lua, node, perl, pygrep, python, r, ruby, rust, script, swift, system but got: 'python_venv'
Check the log at /Users/jesuscaballerorodriguez/.cache/pre-commit/pre-commit.log
```

The solution is to edit file `/Users/jesuscaballerorodriguez/.cache/pre-commit/repoqeelck9u/.pre-commit-hooks.yaml` and replace `language`, so that `python` appears instead of `python_venv`.
