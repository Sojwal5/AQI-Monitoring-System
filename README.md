# AQI-Monitoring-System
# Air Pollution Monitoring System

## Introduction
This project presents an IoT-based Air Pollution Monitoring System that measures indoor harmful gases such as Carbon Dioxide (CO2) using an MQ135 gas sensor and Carbon Monoxide (CO) using an MQ7 sensor. The system displays air quality in Parts Per Million (PPM) on both a 16x2 LCD and on ThingSpeak, facilitating easy monitoring.

## Components Required
- Arduino Uno
- Wi-Fi module Node-MCU ESP8266
- 16x2 LCD
- MQ135 Gas sensor
- MQ7 LPG gas sensor
- Buzzer
- LEDs

## System Architecture
[architecture diagram here]

## Software Requirement
- Arduino IDE for uploading programming to Arduino and Node-MCU boards, with required libraries.
- ThingSpeak for IoT analytics, allowing aggregation, visualization, and analysis of live data streams in the cloud.

## Measurement
Calibrating the sensor in fresh air is crucial, followed by deriving an equation converting sensor output voltage value into convenient units, PPM (Parts Per Million). The mathematical calculations involve finding the slope and applying logarithmic functions for accurate conversion.

## Datasheets
- [MQ135 Datasheet](link-to-datasheet)
- [MQ7 Datasheet](link-to-datasheet)

## Results
```arduino
[Arduino code snippet here]
