# devych_python_flask_server

##Installation
Requirments:
- python 3.8
- Flask
- PyMYsql


## Overview
mysql과 연동하여 api를 제공하는 flask server


##Default Setting
env directory에 env.py를 생성하고, db dict를 생성한다.

```buildoutcfg
db = {
    'host': host,
    'user': user,
    'password': password,
    }
```

위 형식과 같이 db의 주요 정보를 입력한다.