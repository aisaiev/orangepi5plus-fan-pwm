import os
import time
import wiringpi

PWM_PIN = 2
INTERVAL = 5

wiringpi.wiringPiSetup()
wiringpi.pinMode(PWM_PIN, wiringpi.GPIO.OUTPUT)
wiringpi.pwmSetClock(PWM_PIN, 100)
wiringpi.softPwmCreate(PWM_PIN, 0, 100)

def get_cpu_temp():
    raw_temp = int(os.popen("cat /sys/class/thermal/thermal_zone0/temp").read())
    try:
        return float(raw_temp / 1000)
    except():
        raise RuntimeError("Could not get temperature")

def set_fan_speed(speed):
    wiringpi.softPwmWrite(PWM_PIN, speed)

try:
    while True:
        temp = get_cpu_temp()
        if temp < 40:
            set_fan_speed(0)
        elif temp < 50:
            set_fan_speed(25)
        elif temp < 60:
            set_fan_speed(50)
        elif temp < 70:
            set_fan_speed(75)
        else:
            set_fan_speed(100)
        time.sleep(INTERVAL)
except KeyboardInterrupt:
    set_fan_speed(0)