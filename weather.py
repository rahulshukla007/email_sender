#a simple api for fetching the api data
#source -- https://openweathermap.org/api

import requests

try:
  api_key   = "74a493ab4882c6f80635c091aa22d24b"
  base_url  = "http://api.openweathermap.org/data/2.5/weather"

  city = input("please enter a city name: ")   #new york
  request_url = f"{base_url}?q={city}&appid={api_key}"

  response = requests.get(request_url)
  #print(response.status_code)

  if response.status_code == 200:
    data = response.json()
    #print(data)
    weather = data['weather'][0]['description']
    temp    = round((data['main']['temp'] - 273),2) #celsius conversation
    country = data['sys']['country']
    print(f"{country} country {data['name']} city current weather is -- {weather}")
    print(f"{country} country {data['name']} city current temperature is -- {temp}")
  else:
    print("an error occured")

except Exception as e:
  print("Error", e)