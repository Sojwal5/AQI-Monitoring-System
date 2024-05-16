# AQI-Monitoring-System

## Introduction
The AQI (Air Quality Index) Monitoring System is a comprehensive project aimed at providing real
time monitoring and analysis of air quality in a given region. Air pollution is a significant
 environmental and public health concern globally, affecting millions of people. This project seeks to
 address this issue by developing a system that measures various air pollutants and calculates the
 AQI, providing valuable information for decision-makers and the general public.
This project presents an IoT-based Air Pollution Monitoring System that measures indoor harmful gases such as Carbon Dioxide (CO2) using an MQ135 gas sensor and Carbon Monoxide (CO) using an MQ7 sensor. The system displays air quality in Parts Per Million (PPM) on both a 16x2 LCD and on ThingSpeak, facilitating easy monitoring.

## Components Required
 -Raspberry Pi (4B)
 -Nova PM Sensor SDS011
 -MQ 7 – CO gas detection sensor
 -MCP 3008 - 10-bit Analog-to-Digital Converter (ADC) for MQ 7
 -MQ 135 – NH3 gas detection sensor 
 -HDMI cable
 -Male to Male , Male to female , female to female jumper wires
 -Breadboard
 -zero PCB

## System Architecture
[architecture diagram here]

## Software Requirement
-IDE : Thonny, Geany
-Hosting Website : AdaFruit.

## Measurement
Calibrating the sensor in fresh air is crucial, followed by deriving an equation converting sensor output voltage value into convenient units, PPM (Parts Per Million). The mathematical calculations involve finding the slope and applying logarithmic functions for accurate conversion.

## Datasheets
- [MQ135 Datasheet](https://www.olimex.com/Products/Components/Sensors/Gas/SNS-MQ135/resources/SNS-MQ135.pdf)
- [MQ7 Datasheet](https://www.pololu.com/file/0J313/MQ7.pdf)
- [SDS011 Datasheet](https://cdn-reichelt.de/documents/datenblatt/X200/SDS011-DATASHEET.pdf)

##Results
Successful deployment of AQI Monitoring System in the target area.
Real-time monitoring of key air pollutants and calculation of accurate AQI values.
User-friendly interface accessible to both decision-makers and the general public.
Improved awareness of air quality conditions, leading to informed decision-making.
Positive feedback from stakeholders regarding the effectiveness and usability of the system.

## Conclusion
The AQI Monitoring System represents a significant step towards addressing the challenges posed by air pollution. By providing real-time data and insights into air quality conditions, the system empowers individuals, communities, and policymakers to take proactive measures to safeguard public health and the environment. Continued enhancements and collaborations will further strengthen the system's effectiveness in combating air pollution and promoting sustainable development.
