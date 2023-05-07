# Include the library filese
import I2C_LCD_driver
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

#Include the buzzer pin
buzzer = 19

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(buzzer,GPIO.OUT)

# Create a object for the LCD
#lcd = I2C_LCD_driver.lcd()

# Create a object for the RFID module
scan = SimpleMFRC522()


try:
        print("Now place your Tag to scan")      
        print("Place your Tag")                                               
        scan.write("Tag ID")
        id,Tag = scan.read()                    
        print("Your Tag ID is : " + str(id))

    
        GPIO.output(buzzer,GPIO.HIGH)
        sleep(0.5)
        GPIO.output(buzzer,GPIO.LOW)

finally:
        GPIO.cleanup()
