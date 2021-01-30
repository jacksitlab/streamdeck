# streamdeck

## prepare os

```
sudo apt install libhidapi-hidraw0 libudev-dev libusb-1.0-0-dev python3 python3-pip libhidapi-libusb0 libopenjp2-7
```
Add your user to the 'plugdev' group:
```
sudo usermod -a -G plugdev `whoami`

```
Add the udev rules using your text editor:
```
sudo nano /etc/udev/rules.d/99-streamdeck.rules
```
content:
```
SUBSYSTEM=="usb", ATTRS{idVendor}=="0fd9", ATTRS{idProduct}=="0060", MODE:="660", GROUP="plugdev"
SUBSYSTEM=="usb", ATTRS{idVendor}=="0fd9", ATTRS{idProduct}=="0063", MODE:="660", GROUP="plugdev"
SUBSYSTEM=="usb", ATTRS{idVendor}=="0fd9", ATTRS{idProduct}=="006c", MODE:="660", GROUP="plugdev"
SUBSYSTEM=="usb", ATTRS{idVendor}=="0fd9", ATTRS{idProduct}=="006d", MODE:="660", GROUP="plugdev"
```
Reload the rules:
```
sudo udevadm control --reload-rules
```

## run in localenv

### first time
```
pip3 install virtualenv
```
```
virtualenv env
```
```
source env/bin/activate
```
```
pip3 install -r requirements.txt
```

### reinit
```
source env/bin/activate
```

## test connection

```
python3 test/testdeck.py
```

