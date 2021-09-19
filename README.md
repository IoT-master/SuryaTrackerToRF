# Jist of directions

## Will tidy this up later

Transmit Circuit Connection:
VCC = 5v
SIGNAL attaches to GPIO0 or PIN11 BCM17
Receive Circuit Connection:
VCC = 5v
Pin Closest to 5V pin is the signal pin.
Signal Pin to GPI02 or Pin 13 or BCM:R1:21/R2:27
https://i0.wp.com/timleland.com/wp-content/uploads/2014/12/Rf-Wiring-1.png
https://projects.drogon.net/raspberry-pi/wiringpi/pins/
See:
https://projects.drogon.net/raspberry-pi/wiringpi/pins/

https://projects.drogon.net/raspberry-pi/wiringpi/download-and-install/

`git clone https://github.com/wiringpi/wiringpi`

`cd wiringpi`

`./build`

sudo git clone https://github.com/timleland/rfoutlet.git /var/www/rfoutlet
sudo chown root.root /var/www/rfoutlet/codesend
sudo chmod 4755 /var/www/rfoutlet/codesend
/var/www/rfoutlet/codesend <code>
Pulse Length is 189

To sniff out codes:
sudo /var/www/rfoutlet/RFSniffer

Note to self:

https://timleland.com/wireless-power-outlets/

Google
https://timleland.com/use-google-home-to-control-wireless-power-outlets/

https://github.com/WiringPi/WiringPi
https://github.com/WiringPi/WiringPi-Python


https://timleland.com/wireless-power-outlets/