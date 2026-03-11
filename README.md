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
| ... | (Analog output) |

## Files

- `smoke-detector.py` - Basic smoke detector
- `smoke-alert-logger.py` - Smoke detector with Excel logging
- `smoke-monitor.py` - Full smoke monitor with extended logging

## Python Requirements

```bash
pip install pyserial openpyxl twilio
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
