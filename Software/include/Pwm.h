#include "stdint.h"

class Pwm 
{
    public:
        Pwm(uint8_t pin, uint8_t cycleLength);

        void tick();

        void setPulsewidthAbsolute(uint8_t width);

        void setPulsewidthRelative(uint8_t percentage);

    private:
        uint8_t _Cycle;
        uint8_t _Pulsewidth;
        uint8_t _Counter;
        uint8_t _Pin;
};

class FastPwm
{
    public:
        FastPwm(unsigned int frequency);  

        void setPulsewidthRelative(uint32_t percentage);
        void setPulsewidthAbsolute(uint16_t value);

        void init(unsigned int frequency);


    private:
        uint16_t _Top;
};