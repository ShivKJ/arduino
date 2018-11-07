from datetime import timedelta

from light_blinker.modulator import Modulator

if __name__ == '__main__':
    port = '/dev/ttyACM0'

    slow_blink_duration = timedelta(milliseconds=500)
    slow_blink_repition = 4

    fast_blink_duration = timedelta(milliseconds=50)
    fast_blink_repition = 40

    (Modulator(port)
     .min(slow_blink_duration, slow_blink_repition)
     .max(fast_blink_duration, fast_blink_repition)
     .total_blinks(300)
     .close_on_exit()
     .build())
