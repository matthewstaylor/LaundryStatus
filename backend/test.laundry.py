import requests
from datetime import datetime

now = datetime.now()
now = now.strftime('%Y-%m-%d %H:%M:%S')
url = 'http://ec2-52-14-234-1.us-east-2.compute.amazonaws.com/laundry'
myobj = {
    'laundry_status': 'Laundry !',
    'time_posted': now,
    'color': 'green'
}

x = requests.post(url, json = myobj)

print(x.text)