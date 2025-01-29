# Mushroom Environmental Control System

The MECS is the controller for a system to keep the humidity and air-
flow at optimal levels in an environment to grow mushrooms.

The controller runs on a raspberry pi (3+) and manages a
temperature/humidity probe, a humidifier, and a fan.

The system is derived and borrows heavily from the Greenhouse system. In
the process of converting the Greenhouse system, modern methods of
virtual environments, building, testing, and logging are used.


## Goal:
Grow mushrooms by providing an environment with optimal humidity and airflow

## Equipment
- Raspberry pi 3 Model B+
- Temperature/Humidity Sensor SHT4X
- CO2 Sensor SCD4X
- Relay(s)
- Humidifier
- Fan

## Methodology

Use temperature sensor (shtc3) to measure inside temperature and humidity.

Use a tuned PID controllers to run the humidifier and fan.

Enviornmental setpoint, PID K values, and Cycle Time kept in a config
file. Changes to config file trigger reloading of config variables.
Allows for on-the-fly tweeking of parameters.

Temperature, Humidity, CO2, and Power data are sent to initial state
for graphing.

## Setpoints for growing mushrooms

## Pinning

85% - 90% Humidity  
1200ppm - 1500ppm CO2

## Fruiting

80% - 85% Humidity  
500ppm - 800ppm (1000ppm max) CO2

