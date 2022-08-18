# OpenSesame🚪🏃💨
Access control system.
Logs user entry and exit, and opens and locks the door.

## System Requirements
- Raspberry Pi 4B 8GB
- Linux raspberrypi 5.15.56-v8+ #1575 SMP PREEMPT aarch64 GNU/Linux
- Docker version 20.10.17
- docker compose v2.9.0

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

## Setup project
### Clone
```shell
$ git clone https://github.com/salieri256/opensesame-back.git
$ cd opensesame-back/
```

### Create .env
```env
POSTGRES_PASSWORD=****
```

### Enable pigpiod
```shell
$ sudo systemctl enable pigpiod
```

### Build
```shell
$ sudo docker compose build
```

### Start
```shell
$ sudo docker compose up
```

### Reset
```shell
$ docker compose exec db_service poetry run python -m src.migrate_db
```

