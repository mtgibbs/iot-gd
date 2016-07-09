#iot-gd

Prototype RaspberryPi garage door opener written in python utilizing the [GrovePi](http://www.dexterindustries.com/grovepi/).

This prototype uses a relay wired to the garage door opener to activate the door and an ultrasonic ranger to detect of the garage door is up or not.

##Setup on RaspberryPi

  1) Install **[python (2.7)](https://www.python.org/downloads/)**
  
  2) Install **pip**
  
  ```
    sudo apt-get install python-pip
  ```  
  
  3) Install GrovePi dependencies on the pi (full instructions found [here](http://www.dexterindustries.com/GrovePi/get-started-with-the-grovepi/setting-software/)
  
  ```
    cd <directory_for_grovepi>
    sudo git clone https://github.com/DexterInd/GrovePi
    cd <directory_for_grovepi>/GrovePi/Script
    sudo chmod +x install.sh
    sudo ./install.sh
  ```

  4) Install **flask**
  
  ```
    sudo pip install flask
  ```
  
  5) Run by executing **gd-service.py**
  
  ```
    sudo python gd-service.py
  ```
  
##Features to build

- [ ] Integrate into master controller
- [ ] Add security


##License
[Apache 2.0](https://github.com/mtgibbs/iot-gd/blob/master/LICENSE)
