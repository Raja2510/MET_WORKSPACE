
weather={
    "city":"delhi",
    "temperature":35,
    "humidity":45,

}

a=weather["temperature"]
print(a)

weather["wind_speed"]=12

del weather["humidity"]

a=weather.items()
print(a)
print("pressure" in weather)