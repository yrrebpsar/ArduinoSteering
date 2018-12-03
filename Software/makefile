#
#             LUFA Library
#     Copyright (C) Dean Camera, 2012.
#
#  dean [at] fourwalledcubicle [dot] com
#           www.lufa-lib.org
#
# --------------------------------------
#         LUFA Project Makefile.
# --------------------------------------

AVR_ROOT = c:/Daten/Arduino/arduino-1.8.7
AVR=$(AVR_ROOT)/hardware/arduino/avr

MCU          = atmega32u4
ARCH         = AVR8
BOARD        = LEONARDO
F_CPU        = 16000000
F_USB        = $(F_CPU)
OPTIMIZATION = s
TARGET       = ArduinoSteeringWheel
PLATFORM     = ./platform/wiring_digital.c ./platform/Winterrupts.c ./platform/wiring.c
SRC          = main.cpp Descriptors.c XInputPad.cpp Encoder.cpp Pwm.cpp $(LUFA_SRC_USB) $(PLATFORM)
LUFA_PATH    = ./LUFA
CC_FLAGS     = -DUSE_LUFA_CONFIG_HEADER  -DARDUINO=101 -Iinclude/ -IConfig/ -I$(AVR)/cores/arduino -I$(AVR)/variants/leonardo
LD_FLAGS     =

AVRDUDE = $(AVR_ROOT)/hardware/tools/avr/bin/avrdude.exe
AVRDUDE_PROGRAMMER	= avr109
AVRDUDE_PORT	= COM6
AVRDUDE_FLAGS	= -C "$(AVR_ROOT)/hardware/tools/avr/etc/avrdude.conf"

# Default target
all:

# Include LUFA build script makefiles
include $(LUFA_PATH)/Build/lufa_core.mk
include $(LUFA_PATH)/Build/lufa_sources.mk
include $(LUFA_PATH)/Build/lufa_build.mk
include $(LUFA_PATH)/Build/lufa_cppcheck.mk
include $(LUFA_PATH)/Build/lufa_doxygen.mk
include $(LUFA_PATH)/Build/lufa_dfu.mk
include $(LUFA_PATH)/Build/lufa_hid.mk
include $(LUFA_PATH)/Build/lufa_avrdude.mk
include $(LUFA_PATH)/Build/lufa_atprogram.mk
