# Acknowledgements

The steering wheel is built upon [XInputPadMicro](https://github.com/bootsector/XInputPadMicro) which itself is based on the USB stack [LUFA](http://www.fourwalledcubicle.com/LUFA.php). It uses a library for the rotary encoder from [Paul Stoffregen](https://github.com/PaulStoffregen/Encoder).

# Build environment for Windows 10

In order to build the steering wheel firmware, you need the following environment:
* [AVR-IDE](https://www.arduino.cc/en/Main/Software). I have seen some error messages during make process coming from pathes including spaces so it is best to install it at a location without spaces (i.e. not in c:\Program Files\...). I have used version 1.8.7.
* [AVR-GCC](http://gnutoolchains.com/avr/). The toolchain includes GNU `make` but doesn't come with `grep` which has to be installed separately.
* [grep](http://gnuwin32.sourceforge.net/packages/grep.htm). The LUFA makefiles use grep. I have put it in the bin directory of `avr-gcc`.
* [git for windows](https://git-scm.com/download/win) brings `git for windows bash` which understands commands like `rm` needed for `make clean`.

The makefiles redirect some output to `/dev/null` so I had to create a `c:\dev` directory on my notebook to get rid of some error messages.
