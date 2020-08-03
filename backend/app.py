import sys
sys.path.insert(0, "~/.local/lib/python3.6/site-packages")
import pymysql
from flask import Flask, request, jsonify
from datetime import datetime

now = datetime.now()
now = now.strftime('%Y-%m-%d %H:%M:%S')
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World! ' + 'This is the homepage for group 5'


@app.route('/laundry', methods=['POST', 'GET'])
def laundry():
    connection = pymysql.connect(host='mini-project.cfcq26peapme.us-east-2.rds.amazonaws.com',
                                 user='admin',
                                 password='wearegroup5',
                                 db='INDIVIDUAL_PROJECT',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    if request.method=='POST':
        try:
            json = request.json
            laundryStatus = json['laundry_status']
            timePosted = json['time_posted']
            color = json['color']
            with connection.cursor() as cursor:
                sql = "INSERT INTO `LaundryStatus` (`laundry_status`, `time_posted`, `color`) VALUES (%s, %s, %s)"
                data = (laundryStatus, timePosted, color)
                cursor.execute(sql, data)
                connection.commit()
            return 'Successfully posted current laundry data.'
        finally:
            connection.close()

    if request.method=='GET':
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM (SELECT * FROM `LaundryStatus` ORDER BY id DESC LIMIT 1) sub ORDER BY id ASC"
                cursor.execute(sql)
                laundryStatus = cursor.fetchone()
                return jsonify(laundryStatus)
        finally:
            connection.close()