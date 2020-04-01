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

```
$export FLASK_ENV=devlopment
```
flask 환경을 development로 설정한다.


```
$flask run
```
서버를 실행합니다.


## API

| Method           | HTTP request                  | Description                         |
| ---------------- | ----------------------------- | ----------------------------------- |
| get_lotto        | **GET** /lotto/{number}       | {number}회차 로또 정보 가져오기           |
| create_lotto     | **GET** /lotto/create/{number}| {number}회(회당 6개 번호) 로또 번호 생성하기|
| get_lotto_ranking| **GET** /lotto/rank/{number}  | {number} = 1 or 0 <br> 1일 경우 보너스 번호 포함 통계 가져오기<br> 0일 경우 보너스 번호 미포함 통계 가져오기|
