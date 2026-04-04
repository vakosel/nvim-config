import time

from machine import ADC

sensor = ADC(4)

conversion = 3.3 / (65535)

while True:

    reading = sensor.read_u16() * conversion # Voltage 
    temp = 27 - (reading - 0.706) / 0.001721 # Temperature in Celsius
    print("Temperature: {:.2f} °C".format(temp))
    time.sleep(2)





