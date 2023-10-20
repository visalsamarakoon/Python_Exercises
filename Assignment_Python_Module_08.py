# 08. Using relational databases
# Question 01

import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="root",
    password="1234",
    autocommit=True

)

def showairport(icao):
    sql = "SELECT ident, name, iso_country FROM airport"
    sql += " WHERE ident='" + icao + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"The ICAO {row[0]} is of {row[1]} and the country is: {row[2]}")
    return

icao = input("Enter ICAO: ")
showairport(icao)

# Question 02

import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='dbuser',
    password='metropolia',
    autocommit=True
)

def icoa_code(icoa):
    sql = 'SELECT name, type FROM airport'
    sql += ' WHERE iso_country ="'+ icoa + '"' + 'ORDER by type'
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount>0:
        for row in result:
            print(f'Hello! Airport name is {row[0]}. Airport name : {row[1]}')
    return

icoa = input('Enter ICOA:')
icoa_code(icoa

# Question 03

def distancecalculator(airports):
    print(airports)
    sql = "SELECT ID, ident, latitude_deg, longitude_deg FROM airport"
    sql += " WHERE ident='" + icao + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:



