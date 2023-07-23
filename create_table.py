# -*- coding: utf-8 -*-
# Author WU_JUN
from condb import conn

db = conn()

cur = db.cursor()
cur.execute(
    "CREATE TABLE user_info (id INT(10) NOT NULL,name VARCHAR(255), address VARCHAR(255))"
)
