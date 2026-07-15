import time
import board
import adafruit_dht
from RPLCD.i2c import CharLCD
import RPi.GPIO as GPIO
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory  # Import for pigpio support

# Set up the I2C LCD
lcd = CharLCD('PCF8574', 0x27)  # Replace '0x27' with your LCD's I2C address
lcd.clear()

# Set up GPIO for LEDs and Buzzer
GPIO.setmode(GPIO.BCM)
RED_LED_PIN = 17  # Adjust the GPIO pin numbers based on your setup
GREEN_LED_PIN = 27
BUZZER_PIN = 22
GPIO.setup(RED_LED_PIN, GPIO.OUT)
GPIO.setup(GREEN_LED_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# Set up DHT11 sensor
dht_device = adafruit_dht.DHT11(board.D4)  # Adjust GPIO pin as per your setup

# Light sensor pin (LDR)
LDR_PIN = 18  # Example GPIO pin, adjust as per your setup
GPIO.setup(LDR_PIN, GPIO.IN)

# Set up pigpio factory for better PWM control for the Servo motor
factory = PiGPIOFactory()

# Set up the Servo motor (SG90)
servo_pin = 23  # Adjust GPIO pin for the servo motor
servo = Servo(servo_pin, pin_factory=factory)

# Function to read the LDR (light sensor) value
def read_ldr():
    return GPIO.input(LDR_PIN)

# Function to blink the buzzer and red LED 3 times
def alert():
    for _ in range(3):
        GPIO.output(RED_LED_PIN, GPIO.HIGH)
        GPIO.output(BUZZER_PIN, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(RED_LED_PIN, GPIO.LOW)
        GPIO.output(BUZZER_PIN, GPIO.LOW)
        time.sleep(0.5)

# Function to control the fan (servo motor)
def control_fan(state):
    if state == "on":
        # Move servo to simulate fan on (adjust angle as needed)
        servo.max()  # Turn the servo to max (fan "on")
        time.sleep(2)  # Keep the fan "on" for 2 seconds
        servo.min()  # Turn the servo to min (fan "off")
    else:
        # Move servo to its initial position (fan "off")
        servo.min()  # Turn the servo to min (fan "off")
        time.sleep(2)  # Wait for 2 seconds before the next operation

# Main loop
try:
    while True:
        # Read temperature and humidity from DHT11 sensor
        try:
            humidity = dht_device.humidity
            temperature = dht_device.temperature

            if humidity is None or temperature is None:
                raise ValueError("Failed to retrieve data from the sensor")

        except RuntimeError as error:
            print(f"Error reading from DHT11: {error.args}")
            humidity = temperature = None
            time.sleep(2)  # Wait before retrying
            continue

        # Read light sensor value (LDR)
        ldr_value = read_ldr()

        # Display temperature, humidity, and light information on the LCD
        lcd.clear()
        lcd.write_string(f"Temp: {temperature}C")
        lcd.cursor_pos = (1, 0)  # Move to second line
        light_status = "Day" if ldr_value == 1 else "Night"
        lcd.write_string(f"Light: {light_status}")

        # Check if temperature exceeds threshold and activate alerts
        if temperature is not None and temperature > 27:  # Set your own threshold
            # Red LED and buzzer alert
            alert()
            # Turn off Green LED, turn on Red LED
            GPIO.output(GREEN_LED_PIN, GPIO.LOW)
            GPIO.output(RED_LED_PIN, GPIO.HIGH)
            # Control fan (servo motor)
            control_fan("on")  # Turn on the fan (servo motor)
        else:
            # Temperature below threshold
            GPIO.output(GREEN_LED_PIN, GPIO.HIGH)  # Green LED on
            GPIO.output(RED_LED_PIN, GPIO.LOW)  # Red LED off
            # Control fan (servo motor) to off position
            control_fan("off")  # Turn off the fan (servo motor)

        # Sleep before reading again
        time.sleep(2)

except KeyboardInterrupt:
    print("Program interrupted.")
    GPIO.cleanup()  # Cleanup GPIO on exit
