# OpenSesame

## Setup Docker docker-compose
```shell
$ curl -fsSL https://get.docker.com -o get-docker.sh
$ sudo sh get-docker.sh
```

```shell
$ wget https://github.com/docker/compose/releases/download/v2.9.0/docker-compose-linux-aarch64
$ mkdir ~/.docker
$ mv docker-compose-linux-aarch64 ~/.docker/docker-compose
$ chmod +x ~/.docker/docker-compose
```

## Build
```shell
$ sudo docker compose build
```

## Start
```shell
$ sudo docker compose up
```

## .env
```env
POSTGRES_PASSWORD=****
```

## Reset
```shell
$ docker-compose exec api poetry run python -m src.migrate_db
```

