Simple dashboard using nicegui
==============================

This repo shows how it can be possible to use the [nicegui](https://nicegui.io) python library to set up a dashboard
connected to a MQTT broker.

## Dependencies

- python 3.10
- `virtualenv` for python 3.10
- [Just](https://just.systems)
- docker

## How to launch

Simply:

```bash
just serve
```

This should start a mosquitto MQTT broker using docker, initialize the python virtual environment, install the required dependencies, etc.