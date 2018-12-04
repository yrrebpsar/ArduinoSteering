# Idea

It started with this [cool little idea](https://www.thingiverse.com/thing:3049220) that I found on [thingiverse](https://www.thingiverse.com). And it ended up like this...

# Hardware

The base of the steering wheel is an Arduino Pro Micro. It is based on the Atmega 32u4 MCU, which allows us to build an USB slave device. The 
The construction consists of some 3D-printed parts, enhanced by stuff from the local hardware store.

## Shopping List
* [Arduino Pro Micro]()
* [Rotary Encoder KT-040]()
* []

# Software

## Acknowledgements

The steering wheel is built upon [XInputPadMicro](https://github.com/bootsector/XInputPadMicro) which itself is based on the USB stack [LUFA](http://www.fourwalledcubicle.com/LUFA.php). 
The steering wheel position is tracked using a rotary encoder and the encoder-library from [Paul Stoffregen](https://github.com/PaulStoffregen/Encoder).

## Build environment for Windows 10

In order to build the steering wheel firmware, you need the following environment:
* [Arduino-IDE](https://www.arduino.cc/en/Main/Software). I have seen some error messages during make process coming from pathes including spaces so it is best to install it at a location without spaces (i.e. not in c:\Program Files\...). I have used version 1.8.7.
* [avr-gcc](http://gnutoolchains.com/avr/). The toolchain includes GNU `make` but doesn't come with `grep` which has to be installed separately.
* [grep](http://gnuwin32.sourceforge.net/packages/grep.htm). The LUFA makefiles use grep. I have put it in the bin directory of `avr-gcc`.
* [git for windows](https://git-scm.com/download/win) brings `git for windows bash`, which understands commands like `rm`, needed for `make clean`.

The makefiles redirect some output to `/dev/null` so I had to create a `c:\dev` directory to get rid of some error messages.

### Build process
Open a bash window in the `Software` subdirectory of the project. Enter `make` to build the .hex file. 
You can flash the resulting .hex file on the board using a `make avrdude` command. Please make sure, that the Arduino Pro Micro is starting up from reset immediately before issueing the command.

# Further Ideas
* Include accelerator and brake pedals based on the kt-040 rotary encoder.
* Implement a 'drive recorder' that remembers all the timestamps and steering commands and can replay them for the next race. 

