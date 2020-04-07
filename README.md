# devych_python_flask_server


## Installation


Requirments:
- python 3.8
- Flask
- PyMYsql


## Overview

mysql과 연동하여 api를 제공하는 flask server


## Default Setting

env directory에 env.py를 생성하고, db dict를 생성한다.

```buildoutcfg
db = {
    'host': host이름,
    'db': db명
    'user': user명,
    'password': password,
    }
```

위 형식과 같이 db의 주요 정보를 입력한다.

## Run Server

1. git clone을 받고, 아래 명령어를 통해 패키지를 설치한다.
```shell script
$ pip3 install -e .
``` 

2.프로젝트 파일 안 app 디렉토리로 이동한다.

2. 아래 명령어로 서버를 구동한다. 
```shell script
$ python3 webapp.py > /dev/null
```

3. **_ctrl + z_**를 눌러 프로세스를 중단한다.

4. **_bg_**를 입력하고 백그라운드에서 서버를 실행한다.

5. 아래 명령어를 입력한다.
```shell script
$ disown -h
```


## API

| Method           | HTTP request                  | Description                         |
| ---------------- | ----------------------------- | ----------------------------------- |
| get_lotto        | **GET** /lotto/{number}       | {number}회차 로또 정보 가져오기           |
| create_lotto     | **GET** /lotto/create/{number}| {number}회(회당 6개 번호) 로또 번호 생성하기|
| get_lotto_ranking| **GET** /lotto/rank/{number}  | {number} = 1 or 0 <br> 1일 경우 보너스 번호 포함 통계 가져오기<br> 0일 경우 보너스 번호 미포함 통계 가져오기|
