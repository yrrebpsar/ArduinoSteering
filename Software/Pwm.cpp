#include "Arduino.h"
#include "Pwm.h"

Pwm::Pwm(uint8_t pin, uint8_t cycle)
{
    _Cycle = cycle;
    _Pulsewidth = 0;
    _Counter = 0;
    _Pin = pin;
    pinMode(pin, OUTPUT);
}

void Pwm::setPulsewidthAbsolute(uint8_t width)
{
    _Pulsewidth = width;
}

void Pwm::setPulsewidthRelative(uint8_t percentage) 
{
    _Pulsewidth = _Cycle * percentage / 100;
}

void Pwm::tick() 
{
    _Counter = (_Counter + 1) % _Cycle;
    if (_Counter == _Pulsewidth) 
    {
        digitalWrite(_Pin, LOW);
    } 
    if (_Counter == 0 && _Counter < _Pulsewidth)
    {
        digitalWrite(_Pin, HIGH);
    }
}

FastPwm::FastPwm(unsigned int f) 
{
}

void FastPwm::init(unsigned int f) 
{
        // TCCR1A
    //      |  7  |  6  |  5  |  4  |  3  |  2  |  1  |  0  |
    //      |   COM1A   |   COM1B   |   COM1C   |  WGM1 1:0 |  
    TCCR1A =              (0b10<<4) |                0b11;


    // TCCR1B
    //      |  7  |  6  |  5  |  4  |  3  |  2  |  1  |  0  |
    //      |ICNC1|ICES1|  -  |  WGM1 3:2 |       CS1       |
    TCCR1B =                     (0b11<<3)|      0b001;

    _Top = 16000000/f;
    OCR1A = _Top;

    pinMode(PIN_A10, OUTPUT);
    // DDRB|=1<<6;    // Set Output Mode B6

}

void FastPwm::setPulsewidthRelative(uint32_t percentage)
{
    uint16_t value;
    switch (percentage)
    {
        case 0: 
            value = _Top;
            break;
        case 100:
            value = _Top-1;
            break;
        default:
            value = percentage * _Top / 100;
            break;
    }
    OCR1B = value;
}

void FastPwm::setPulsewidthAbsolute(uint16_t value)
{
    OCR1B = value % _Top;
}
