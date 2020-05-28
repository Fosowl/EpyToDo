##
## EPITECH PROJECT, 2020
## controller
## File description:
## controller
##

from flask import Flask, request, render_template
import pymysql.cursors
import jinja2

class interact:
    def __init__(self):
        self.user = None
    
    def disconnect_user(self, connection):
        disconnect = connection.close()
        return disconnect

    def connect_in(self, connection):
        recup_name_user = request.form['user_name']
        recup_password_user = request.form['user_password']
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `password` FROM `user` WHERE `username`=%s"
            cursor.execute(sql, (recup_name_user,))
            result = cursor.fetchone()
            if (result[0] != recup_password_user or result == None):
                return 1
        connection.commit()

    def register_user(self, connection):
        recup_name_user = request.form['user_name']
        recup_password_user = request.form['user_password']
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `user` (`username`, `password`) VALUES (%s, %s)"
            cursor.execute(sql, (recup_name_user, recup_password_user))
        connection.commit()
        return 0