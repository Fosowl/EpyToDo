##
## EPITECH PROJECT, 2020
## models
## File description:
## models
##

from app import *
import pymysql as sql
import pymysql.cursors

class connection_data:
    def __init__(self):
        self.connect = None
        self.connection(app.config)

    def connection(self, config):
        self.connect = sql.connect(host = config['DATABASE_HOST'], user = config['DATABASE_USER'], password = config['DATABASE_PASS'], db = config['DATABASE_NAME'])

    def rtn_connect(self):
        return self.connect