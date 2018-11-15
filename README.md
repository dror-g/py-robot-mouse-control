# Python robot mouse control

## Overview
These scripts allow for capturing mouse movements and sending them as servo instructions over Bluetooth to a BBC Micro:Bit robot.  

## Requirements
### Mouse control script
In order to send instructions over Bluetooth Low-Energy we use the excellent [pygattlib](https://bitbucket.org/OscarAcena/pygattlib).  
Follow the installation instructions at the pygattlib [repo](https://bitbucket.org/OscarAcena/pygattlib), not forgetting to install the dependencies listed in the `DEPENDS` file.  
  
Then, alter the Bluetooth device MAC address in `mouse-control.py` to use your device address.  
  
You can run the `mouse-control.py` script from your laptop, or as I do - from a Raspberri Pi.  

### Micro:Bit robot
After assembling your Micro:Bit robot (aka Micro:Bot), deploy the "mouse-control.js" script to your bot using [Microsoft MakeCode](https://makecode.microbit.org).  
  
First, create a new project.  
Then, from the block components scroll bar (where "Basic, Input, Loops.." are listed) - click "Extensions" at the very bottom.  
Select "Bluetooth" and click "OK/accept" on the warning that's presented.  
  
Now click on the gear/cog at the top right of the screen and select "Project Settings".  
Then select "No Pairing Required", which will enable you to connect to your bot more easily (but don't leave it unsupervised..).  

Last, swith from Blocks view to Javascript at the top-center of the screen,  
Delete all Javascript code in the editor and paste the contents of `mouse-control.js`.  
  
Click "Download" and install the resulting hex-file to your Micro:Bot (by dragging it to the Microbit drive when connected to PC).  

## Usage
Run `sudo python mouse-control.py`.  

