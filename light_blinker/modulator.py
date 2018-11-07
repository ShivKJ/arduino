from functools import partial

from light_blinker.blink_code import blink


def _modulator(t, min_freq=3, max_freq=8, time_period=10):
    remainder = t % time_period

    if remainder < 5:
        return 1 / min_freq
    else:
        return 1 / max_freq


class Modulator:
    def __init__(self, port):
        self._port = port
        self._min_freq = None
        self._max_freq = None
        self._time_period = None

    def min_frequency(self, freq):
        self._min_freq = freq
        return self

    def max_frequency(self, freq):
        self._max_freq = freq
        return self

    def time_period(self, time_period):
        self._time_period = time_period
        return self

    def build(self):
        _mod = partial(_modulator,
                       min_freq=self._min_freq,
                       max_freq=self._max_freq,
                       time_period=self._time_period)

        blink(self._port, _mod)
