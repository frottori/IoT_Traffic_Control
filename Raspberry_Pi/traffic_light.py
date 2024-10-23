from gpiozero import TrafficLights
from time import sleep
import requests

key = "R1LCUDBNUIP9GOW3"

def updateData(redStatus, greenStatus, amberStatus):
    x = requests.get(f"https://api.thingspeak.com/update?api_key=" + key + "&field1=" + redStatus + "&field2=" + greenStatus + "&field3=" + amberStatus)
    if (x.status_code == 200):
        print(f"Red: {redStatus}, Yellow: {amberStatus}, Red: {redStatus}")
        print(F"Entry: "+ x.text)
    else:
        print(f"Failed to update, Response: {x.status_code}")

if __name__ == "__main__":
    # Option 1: With TrafficLights
    lights = TrafficLights(25, 8, 7)
    while True:
        # Red light on and off
        lights.red.on()
        updateData("1", "0", "0")
        sleep(30)
        
        # Green light on and off
        lights.red.off()
        lights.green.on()
        updateData("0", "1", "0")
        sleep(30)
        
        # Amber light on and off
        lights.green.off()
        lights.amber.on()
        updateData("0", "0", "1")
        sleep(20)
        lights.amber.off()

# Option 2: With Three Different LEDs
# red = LED(25)
# yellow = LED(8)
# green = LED(7)

# leds = [red, green, yellow]
# while True:
#     for led in leds:
#         led.on()
#         if (led == yellow):
#             sleep(20)
#         else:
#             sleep(30)
#         led.off()
