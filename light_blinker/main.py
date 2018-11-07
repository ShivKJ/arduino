from light_blinker.blink_code import blink
from light_blinker.modulator import Modulator

if __name__ == '__main__':
    port = '/dev/ttyACM0'
    modulator = Modulator().min_frequency(3).max_frequency(30).time_period(10).build()
    blink(port, modulator)
