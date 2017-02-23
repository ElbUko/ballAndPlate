import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
p = GPIO.PWM(11, 50)     # 50 pulsos por seg al pin 2 en modo pwm
p.start(7.5)            #Pulso del 7.5% para centrarlo

try:
    while True:
        p.ChangeDutyCycle(4.5)
        time.sleep(0.5)
        p.ChangeDutyCycle(10.5)
        time.sleep(0.5)
        p.ChangeDutyCycle(7.5)
        time.sleep(0.5)

except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
