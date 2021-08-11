
## Mosquitto Configuration and Authentication

* On your Raspberry Pi (or Host where Nodered and Mosquitto is installed)
```
cd /etc/mosquitto/conf.d/

# Create a .conf file if it is already not present
touch mosquitto.conf

# Giver port and path to password_file
port 1883
password_file /etc/mosquitto/passwords.txt
allow_anonymous false

# Create a new file passwords.txt
cd ../
vim passwords.txt

# Add your usernames and passwords in this file
abc:password
abc2:password2

# Make sure to make a copy of these somewhere before encrypting them

# Encrypt them
sudo mosquitto_passwd -U passwords.txt

# Restart Mosquitto service
sudo service mosquitto restart



# EspMQTTClient
