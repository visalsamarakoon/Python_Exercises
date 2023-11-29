# 13. Setting up a backend service with an interface

# Question 01

from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/prime_number/<int:number>', methods=['GET'])
def check_prime(number):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = {"Number": number, "isPrime": is_prime(number)}
    response_data = json.dumps(result)
    return response_data, 200, {'Content-Type': 'application/json'}


if __name__ == '_main_':
    app.run(debug=True, host='127.0.0.1', port=5000)

# ----------------------------------------------------------------------------------------------------------------------


# Question 02

from flask import Flask, Response
import json
import mysql.connector

app = Flask(__name__)


@app.route('/airport/<icao>', methods=['GET'])
def get_airport_info(icao):
    connection = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='1234',
        database='flight_game'
    )
    cursor = connection.cursor()

    query = f"SELECT name, municipality FROM airport WHERE name = %s"
    cursor.execute(query, (icao,))

    airport_info = cursor.fetchone()

    if airport_info:
        response_data = {
            "ICAO": icao.upper(),
            "Name": airport_info[0],
            "Location": airport_info[1]
        }
        connection.close()
        response_json = json.dumps(response_data)
        return Response(response_json, status=200, content_type='application/json')

    connection.close()
    return Response(status=404)


if __name__ == '_main_':
    app.run(debug=True)