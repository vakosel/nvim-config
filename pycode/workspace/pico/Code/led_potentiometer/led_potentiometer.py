from machine import ADC, PWM, Pin
from utime import sleep

pot = ADC(Pin(26))  # potentiometer connected to pin 26
led = PWM(Pin(15))  # LED connected to pin 15

led.freq(1000)  # set PWM frequency to 1kHz


try:
    while True:
        raw = pot.read_u16()
        percent = int((raw / 65535) * 100)
        duty = int((percent / 100) * 65535)

        led.duty_u16(duty)
        print("Brightness:", percent, "%")
        sleep(0.05)

except KeyboardInterrupt:
    led.deinit()  # stop PWM completely
    pin = Pin(15, Pin.OUT)
    pin.value(0)  # turn off LED
    print("PWM stopped, LED off")
