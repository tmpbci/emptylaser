Empty Laser 
By Sam Neurohack
LICENCE : CC

Needs : an etherdream DAC, an ILDA laser, RJ 45 IP network
 
You get a basic pygame skeleton to handle the laser drawing with an onscreen simulator.
This Empty Laser is mainly a Laser Hexagon (see /tmp/lab github) structure with some extras, like alignement keys.

Install :

Pygame and its dependancies.

To run : 

python main.py


For easy bootstrapping your project, this program displays example code for  

- some kind of living points for a nice laser harp effect.
- a square you can drive with arrow keys.


Look at LaserHexagon for advanced display and technique.


Many things are still in the todo list as how to store the align parameters in globalVars for the next run.

This program suppose that the ether dream is auto configured in a certain way especially for its IP address. Write an autoplay.txt file inside an SD Card within the ether dream DAC, with the following lines you can adjust i.e for pps or fps. Yes, there is a builtin DHCP client in the ether dream DAC but if you run multiple lasers, having a fixed dedicated network makes you focus on laser stuff.

/net/ipaddr 192.168.1.3
/net/netmask 255.255.255.0
/net/gateway 192.168.1.1
/ilda/pps 25000
/ilda/fps 25

About hardware setup, especially if you have several lasers : ILDA cables are insanely expensive. You may consider the Power Over Ethernet 'POE' option. Buy a very small ILDA cable, a POE splitter and connect everything to the ether dream fixed near your laser. You can have then a simple and very long network cable and use a Power Over Ethernet injector or switch closed to the driving computer. Beware some vendors use 24V POE Injector : POE injectors and splitters must match.
