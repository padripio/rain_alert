import requests

import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
sid="AC3b331a0a36770ec9e5bf4b7aa97d1e9e"
auth="9acc6726a3e38a22fb699c3977b9e791"
account_sid = os.environ.get("SID")
auth_token = os.environ["AUTH"]
twilio_phone = "+12184233208"
my_phone = "+254792960165"
print(f"sid : {account_sid} auth : {auth_token}")

api_key = os.environ["API_KEY"]
parameters = {"lat": "-1.189310", "lon": "37.116371", "key": api_key, "hours": "12"}
response = requests.get(url="http://api.weatherbit.io/v2.0/forecast/hourly", params=parameters)
data = response.json()
print(data.json())
weather_dict = data["data"]
will_rain = 0
for x in weather_dict:
    code = int(x["weather"]["code"])
    if code < 700:
        will_rain = 1

if will_rain == 1:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Goat Goat ,its going to rain today\n Carry an umbrella ☂️ ",
        from_=twilio_phone,
        to=my_phone
    )

    print(message.status)
