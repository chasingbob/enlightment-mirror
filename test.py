import json
import config
import weather
import route

c = config.get_value('openweather_key')
print(c)

e = weather.get_current_weather()
print(e)

t = route.get_current_traffic('8 Bobby Locke road Randburg','2 Impala ave Sandton')
print(t)

