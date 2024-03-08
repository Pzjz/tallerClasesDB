import mysql.connector

def connect(host,user,password,database):
    connection = mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="",
        db="taller1")
    return connection