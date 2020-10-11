import requests
import json

# get 9 day forecast api data
data_9_day_forecast = requests.get('https://pda.weather.gov.hk/locspc/data/fnd_e.xml')

# print api response code
print("The response code is "+str(data_9_day_forecast.status_code))

# load response by json
data_9_day_forecast_json = json.loads(data_9_day_forecast.content)

# log the second data in json
max_rh = data_9_day_forecast_json["forecast_detail"][1]["max_rh"]
min_rh = data_9_day_forecast_json["forecast_detail"][1]["min_rh"]
forecast_date = data_9_day_forecast_json["forecast_detail"][1]["forecast_date"]

# print out logged data
print("On "+str(forecast_date)+", the relative humidity is "+str(min_rh)+"% - "+str(max_rh)+"%")