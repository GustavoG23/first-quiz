def get_city_temperature(city):
   if city == "Quito":
      return 22
   if city == "Sao Paulo":
      return 17
   if city == "San Francisco":
      return 16
   if city == "New York":
      return 14  
   return None


def get_city_weather(city):
  sky_condition = None

  if city == "Sao Paulo":
     sky_condition = "cloudy"
  elif city == "New York":
     sky_condition = "rainy"

  temperature = get_city_temperature(city)

  if temperature is not None:
    return str(temperature) + " degrees and " + (sky_condition if sky_condition is not None else "sunny")
  else:
    return "Desconocido"
