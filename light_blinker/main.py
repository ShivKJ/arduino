from light_blinker.modulator import Modulator

if __name__ == '__main__':
    port = '/dev/ttyACM0'
    Modulator(port).min_frequency(3).max_frequency(30).time_period(10).build()
