# OpenSesame

## .env
```env
POSTGRES_PASSWORD=****
```

## Reset
```shell
$ docker-compose exec api poetry run python -m src.migrate_db
```

