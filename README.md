# Orange Pi 5 Plus Fan PWM control

Tested on [ubuntu-rockchip](https://github.com/Joshua-Riek/ubuntu-rockchip)

1. Install wiringOP-Python
 - sudo apt-get update
 - sudo apt-get -y install git swig python3-dev python3-setuptools
 - git clone --recursive https://github.com/orangepi-xunlong/wiringOP-Python -b next
 - cd wiringOP-Python
 - git submodule update --init --remote
 - python3 generate-bindings.py > bindings.i
 - sudo python3 setup.py install
2. Turn On PWM14_M2
 - sudo nano /boot/firmware/ubuntuEnv.txt
 - add pwm14-m2 to overlays, example: overlays=uart3 usbhost2 usbhost3 pwm14-m2
 - reboot
 - check if pwm14-m2 is turned on
    - ls /sys/class/pwm -l
    - result should contain "pwmchip2 -> ../../devices/platform/febf0020.pwm/pwm/pwmchip2"
3. Enable auto start
 - sudo crontab -e
 - add line to the end of file "@reboot python3 path_to_script &"
 - reboot
