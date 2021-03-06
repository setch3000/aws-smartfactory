# aws-sensor-data-simulator

## Introduction

This simulator generates data based on config JSON file.
The config JSON file has 'checkPoint' porperty to specifiy the value on the designated timesatamp.

## how to run

pubsub_simulator_training.py : data generator for training

``` python
pubsub_simulator_training.py --endpoint awaztwvri1f9k-ats.iot.us-east-1.amazonaws.com --cert 56d1a0401f-certificate.pem.crt --key 56d1a0401f-private.pem.key --topic iot/sensors
```

pubsub_simulator_inference.py : data generator for inference

``` python
pubsub_simulator_inference.py --endpoint awaztwvri1f9k-ats.iot.us-east-1.amazonaws.com --cert 56d1a0401f-certificate.pem.crt --key 56d1a0401f-private.pem.key --topic iot/sensors
```

## Examople config JSON file

```json
{
    "sensors": [
        {
            "name" : "rVibration_Temp",
            "upperThreshold" : 100,
            "lowerThreshold" : 0,
            "iniitalValue" : 50,
            "checkPoint" : [
                {
                    "timestamp": "00:00:00.000000",
                    "value": 30
                }, 
                {
                    "timestamp": "01:00:00.000000",
                    "value": 35
                },
                {
                    "timestamp": "02:00:00.000000",
                    "value": 40
                },
                {
                    "timestamp": "03:00:00.000000",
                    "value": 45
                },
                {
                    "timestamp": "04:00:00.000000",
                    "value": 50
                },
                {
                    "timestamp": "05:00:00.000000",
                    "value": 55
                },
                {
                    "timestamp": "06:00:00.000000",
                    "value": 60
                },
                {
                    "timestamp": "07:00:00.000000",
                    "value": 65
                },
                {
                    "timestamp": "08:00:00.000000",
                    "value": 70
                },
                {
                    "timestamp": "09:00:00.000000",
                    "value": 75
                },
                {
                    "timestamp": "10:00:00.000000",
                    "value": 80
                },
                {
                    "timestamp": "11:00:00.000000",
                    "value": 85
                },
                {
                    "timestamp": "12:00:00.000000",
                    "value": 90
                },
                {
                    "timestamp": "13:00:00.000000",
                    "value": 85
                },
                {
                    "timestamp": "14:00:00.000000",
                    "value": 80
                },
                {
                    "timestamp": "15:00:00.000000",
                    "value": 75
                },
                {
                    "timestamp": "16:00:00.000000",
                    "value": 70
                },
                {
                    "timestamp": "17:00:00.000000",
                    "value": 65
                },
                {
                    "timestamp": "18:00:00.000000",
                    "value": 60
                },
                {
                    "timestamp": "19:00:00.000000",
                    "value": 55
                },
                {
                    "timestamp": "20:00:00.000000",
                    "value": 50
                },
                {
                    "timestamp": "21:00:00.000000",
                    "value": 45
                },
                {
                    "timestamp": "22:00:00.000000",
                    "value": 40
                },
                {
                    "timestamp": "23:00:00.000000",
                    "value": 35
                }
            ]

        }
    ]
}
```

## Example data generated by this simulator

```json

{
    "rVibration_Temp": 77.19,
    "rVibration_Z_RMS_Velocity": 104.38,
    "rVibration_X_RMS_Velocity": 35.62,
    "wRMSCurrent": 108.44,
    "wCurrentLoad": 109.44,
    "wEncoderVelocity": 2587.56,
    "wCylinderStatus": 1.0,
    "sDateTime": "2020-02-26 14:33:44.273"
}

```
