import requests
from twilio.rest import Client


account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token  = "your_auth_token"


response = requests.get("https://api.openweathermap.org/data/2.5/forecast?"
                        "lat=-3.732714&lon=-38.526997&cnt=4&appid=fe36f9b70f72cde6225b3e8e81ba863c")
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to="+995579164807",
        from_="+15642444257",
        body="It's going to rain today. Remember to bring an ☔!"
    )

    print(message.status)
