# Smoke Detector & Alert System

A complete IoT project for detecting smoke using MQ-135 sensor with SMS and call alerts.

## Components

- **Arduino** (Mega/Uno)
- **MQ-135 Smoke/Gas Sensor**
- **Relay Module** (optional for buzzer)
- **Buzzer** (optional)

## Hardware Setup

| Pin | Component |
|-----|-----------|
| A0  | MQ-135 Sensor |

## Connection Diagram

```
┌─────────────┐         ┌─────────────┐
│   Arduino   │────────▶│    MQ-135   │
│    Mega     │         │  Smoke      │
│             │         │  Sensor     │
│  Pin A0 ────┤         └─────────────┘
└──────┬──────┘
       │
       ▼ USB
┌─────────────┐
│     PC      │
│  (Python    │
│  Script)    │
│             │
│  Twilio     │
│  (SMS/Call) │
└─────────────┘
```

## Data Flow

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   MQ-135     │────▶│   Arduino    │────▶│     PC       │
│   Sensor     │     │   (A0 Pin)  │     │  (COM Port)  │
└──────────────┘     └──────────────┘     └──────┬───────┘
                                                  │
                    ┌──────────────┐              │
                    │   Twilio     │◀─────────────┘
                    │ (SMS/Call)   │
                    └──────────────┘
                                                  │
                    ┌──────────────┐              │
                    │ Excel File   │◀─────────────┘
                    │   (.xlsx)    │
                    └──────────────┘
```

## Files

- `smoke-detector.py` - Basic smoke detector
- `smoke-alert-logger.py` - Smoke detector with Excel logging
- `smoke-monitor.py` - Full smoke monitor with extended logging

## Python Requirements

```bash
pip install pyserial openpyxl twilio
```

## Configuration

Edit the Python files and replace placeholder credentials:

```python
TWILIO_ACCOUNT_SID = 'YOUR_ACCOUNT_SID'
TWILIO_AUTH_TOKEN = 'YOUR_AUTH_TOKEN'
TWILIO_PHONE_NUMBER = '+1234567890'
TARGET_PHONE_NUMBER = '+1234567890'
arduino_port = 'COM4'  # Update to your Arduino port
```

## How to Get Twilio Credentials

### Step 1: Create Twilio Account
1. Go to [twilio.com](https://www.twilio.com) and sign up
2. Verify your email and phone number

### Step 2: Get Your Credentials
1. Log in to [console.twilio.com](https://console.twilio.com)
2. Find your **Account SID** on the dashboard
3. Create an **Auth Token** (or use existing one)

### Step 3: Get a Phone Number
1. Go to **Phone Numbers** → **Manage** → **Buy a number**
2. Search for available numbers
3. Purchase a number (they provide free credits for testing)

### Step 4: Update Python Scripts
Replace the placeholders with your actual credentials:

```python
TWILIO_ACCOUNT_SID = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'  # From Twilio Console
TWILIO_AUTH_TOKEN = 'your_auth_token'                       # From Twilio Console
TWILIO_PHONE_NUMBER = '+1234567890'                         # Your Twilio phone number
TARGET_PHONE_NUMBER = '+9876543210'                        # Your personal phone number
```

### Note
- Free trial accounts can only send to verified phone numbers your phone
- Add number in **Verified Caller IDs** section

## Usage

1. Upload Arduino sketch (smoke sensor code) to Arduino
2. Run any Python script on PC
3. Connect Arduino via USB (COM4)
4. When smoke level > 300, alerts are triggered

## Alert Features

- SMS notification via Twilio
- Phone call alert
- Excel logging

## Output Format

```
Smoke Level: 150
Smoke Level: 320
Smoke detected! Triggering alerts...
SMS alert sent.
Call alert initiated.
```
