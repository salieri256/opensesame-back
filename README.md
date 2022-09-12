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
./db/.env
```env
POSTGRES_PORT=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=
```

./db_service/.env
```env
DB_HOST=
DB_PORT=
DB_USER=
DB_PASSWORD=
DB_NAME=
API_PORT=
ALLOW_ORIGINS=[]
ALLOW_METHODS=[]
ALLOW_HEADERS=[]
ALLOW_CREDENTIALS=
```

./door_lock/.env
```env
PWM_PIN=
API_PORT=
ALLOW_ORIGINS=[]
ALLOW_METHODS=[]
ALLOW_HEADERS=[]
ALLOW_CREDENTIALS=
```

./nfc_activity/.env
```env
DB_SERVICE_BASE_URL=
DEVICE_PATH=
```

./nfc_lock/.env
```env
DB_SERVICE_BASE_URL=
DOOR_LOCK_BASE_URL=
DEVICE_PATH=
DOOR_ID=
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

## .env Example
![system](https://user-images.githubusercontent.com/56764525/187325354-d9f942b4-ffe6-4e2c-b8f9-edcc56511651.png)

./db/.env
```env
POSTGRES_PORT=5432
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=postgres
```

./db_service/.env
```env
DB_HOST=192.168.0.2
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=postgres
DB_NAME=postgres
API_PORT=8000
ALLOW_ORIGINS=["*"]
ALLOW_METHODS=["*"]
ALLOW_HEADERS=["*"]
ALLOW_CREDENTIALS=False
```

./door_lock/.env
```env
PWM_PIN=12
API_PORT=8001
ALLOW_ORIGINS=["*"]
ALLOW_METHODS=["*"]
ALLOW_HEADERS=["*"]
ALLOW_CREDENTIALS=False
```

./nfc_activity/.env
```env
DB_SERVICE_BASE_URL=http://192.168.0.3:8000
DEVICE_PATH=usb
```

./nfc_lock/.env
```env
DB_SERVICE_BASE_URL=http://192.168.0.3:8000
DOOR_LOCK_BASE_URL=http://192.168.0.4:8001
DEVICE_PATH=usb
DOOR_ID=1
```
