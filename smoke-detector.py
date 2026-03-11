import serial
import time
from twilio.rest import Client

# Twilio credentials (replace with your own)
TWILIO_ACCOUNT_SID = "YOUR_ACCOUNT_SID"
TWILIO_AUTH_TOKEN = "YOUR_AUTH_TOKEN"
TWILIO_PHONE_NUMBER = "+1234567890"
TARGET_PHONE_NUMBER = "+1234567890"

# Serial communication settings
arduino_port = "COM4"  # Update this to the correct port
baud_rate = 9600

# Initialize Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


def send_sms():
    """Send an SMS alert using Twilio."""
    try:
        message = client.messages.create(
            body="ALERT: Smoke detected! Please evacuate immediately.",
            from_=TWILIO_PHONE_NUMBER,
            to=TARGET_PHONE_NUMBER,
        )
        print("SMS alert sent.")
    except Exception as e:
        print(f"Failed to send SMS: {e}")


def make_call():
    """Make a call alert using Twilio."""
    try:
        call = client.calls.create(
            to=TARGET_PHONE_NUMBER,
            from_=TWILIO_PHONE_NUMBER,
            url="http://demo.twilio.com/docs/voice.xml",  # TwiML URL
        )
        print(f"Call alert initiated. Call SID: {call.sid}")
    except Exception as e:
        print(f"Failed to make a call: {e}")


# Initialize serial connection
print("Initializing serial connection...")
try:
    arduino = serial.Serial(arduino_port, baud_rate, timeout=1)
    time.sleep(2)  # Allow time for Arduino to stabilize
    print("Serial connection established!")
except serial.SerialException as e:
    print(f"Error: Could not open port {arduino_port}. {e}")
    exit(1)

# Main loop to listen for smoke level data
print("Listening for commands from Arduino...")
try:
    while True:
        if arduino.in_waiting > 0:
            # Read and process the smoke level
            message = arduino.readline().decode().strip()

            if message.isdigit():  # Check if the message is numeric
                smoke_level = int(message)
                print(f"Smoke Level: {smoke_level}")

                # Trigger alerts if smoke level exceeds threshold
                if smoke_level > 300:  # Adjust threshold as needed
                    print("Smoke detected! Triggering alerts...")
                    send_sms()
                    make_call()
                    print("Alert process completed.")  # Confirm after both alerts
                    time.sleep(10)  # Delay to prevent duplicate alerts

        time.sleep(1)  # Polling delay

except KeyboardInterrupt:
    print("Program terminated by user.")

finally:
    arduino.close()
    print("Serial connection closed.")
