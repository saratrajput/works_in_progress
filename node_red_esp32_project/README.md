# Node-RED ESP32 Project

### Setting hostname on Raspberry Pi

* Open raspi-config utility
```
sudo raspi-config
```

* Go to network options
![Network Options](images/raspi_config_network_options.png)

* Change hostname
![Change Hostname](images/raspi_config_change_hostname.png)

* Change it to a reasonable name. For eg:

```
nodered.local
```


sudo npm install -g --unsafe-perm node-red
sudo apt install mosquitto mosquitto-clients
