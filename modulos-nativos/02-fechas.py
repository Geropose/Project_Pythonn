# import time

# print(time.time())

from datetime import datetime

fecha = datetime(2023, 1, 1)
fecha2 = datetime(2023, 1, 1)
ahora = datetime.now()

print(ahora)

fechaStr = datetime.strptime("2023-01-03", "%Y-%m-%d")
print(fechaStr)

print(fecha.strftime("%Y.%m.%d"))
