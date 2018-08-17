

## Control de la matriz de LEDs con Python
https://codeclubprojects.org/en-GB/sense-hat/countdown-timer/
```
displaying-images.py
question_mark.py
countdown.py  # 60 segundos
```
## Control de la matriz de LEDs desde Node-RED
https://flows.nodered.org/node/node-red-node-pi-sense-hat
```
node-red-LED_matrix.json
```

## Sensado del ambiente y simulador
#### Temperatura, humedad y presión
https://medium.com/@jeancarlbisson/node-red-iot-workshop-using-raspberry-pi-and-sense-hat-sensor-866ae4bcaf4a
https://github.com/jeancarl/node-red-labs/tree/master/lab-sense-hat/iot-starter
```
Environment-temp_hum_pressure(real_and_simulated).json
```
## INSTALLATION

#### SENSE HAT: Install the python library
https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat/2
```
sudo apt-get install sense-hat
```
#### SIMULATOR: Install the python library
https://www.raspberrypi.org/blog/desktop-sense-hat-emulator/
#### For Ubuntu
```
sudo add-apt-repository ppa://waveform/ppa
sudo apt-get update
sudo apt-get install python-sense-emu python3-sense-emu sense-emu-tools
```
#### For Raspbian
```
sudo apt-get update
sudo apt-get install python-sense-emu python3-sense-emu python-sense-emu-doc sense-emu-tools -y
```

#### Other platforms
pip install sense-emu
#### Upgrade
pip install -U sense-emu
#### Remove
pip uninstall sense-emu
