# {{ cookiecutter.project_name }}


## Docker compose

To run with docker compose, run this:

```bash
docker-compose down -v
docker-compose up
```

The first command is so that we can remove dangling container and volumes, from previous docker runs.