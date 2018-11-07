from datetime import timedelta

from light_blinker.modulator import Modulator

if __name__ == '__main__':
    port = '/dev/ttyACM0'
    slow = timedelta(milliseconds=500)
    fast = timedelta(milliseconds=50)

    Modulator(port).min(slow, 4).max(fast, 50).build()
