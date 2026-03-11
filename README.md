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
