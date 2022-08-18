import requests
from bs4 import BeautifulSoup

### Build query
URL = "https://weather.com/weather/today/l/b1d7089dcff056d6907ce58c458f2a32932387f1854af523080c6c79e2678e66"
htmlPage = requests.get(URL)
beautifulSoup = BeautifulSoup(htmlPage.content, "html.parser")

### Parse the results
results = beautifulSoup.find(id="WxuCurrentConditions-main-eb4b02cb-917b-45ec-97ec-d4eb947f6b6a")
currentTemp = results.find("span", class_="CurrentConditions--tempValue--3a50n")
description = results.find("div", class_="CurrentConditions--phraseValue--2Z18W")
location = results.find("h1", class_="CurrentConditions--location--kyTeL")
timeOfDay = results.find("span", class_="CurrentConditions--timestamp--23dfw")

### Print results to user
print("Current temperature:", currentTemp.text)
print("Weather description:", description.text)
print("Location:", location.text)
print("Local time:", timeOfDay.text)
