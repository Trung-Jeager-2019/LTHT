import RPi.GPIO as GPIO
from signal import pause

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

GPIO.output(17, 1)

pause()

try:
    pass
except KeyboardInterrupt:
    pass
except:
    pass
finally:
    GPIO.cleanup()
