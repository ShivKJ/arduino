from datetime import timedelta

from light_blinker.blink_code import blink


class Modulator:
    def __init__(self, port, baudrate=9600):
        self._port = port
        self._baudrate = baudrate

        self._min = None
        self._min_rep = None

        self._max = None
        self._max_rep = None

        self._total_blinks = None

        self._close_on_exit = False

    def min(self, time_duration: timedelta, repetition: int):
        self._min = time_duration.total_seconds()
        self._min_rep = repetition

        return self

    def max(self, time_duration: timedelta, repetition: int):
        self._max = time_duration.total_seconds()
        self._max_rep = repetition

        return self

    def total_blinks(self, blinks):
        self._total_blinks = blinks
        return self

    def close_on_exit(self):
        self._close_on_exit = True

        return self

    def build(self):
        time_period = self._min_rep + self._max_rep

        def process(t):
            remainder = t % time_period

            if remainder < self._min_rep:
                return self._min

            return self._max

        blink(self._port, process, baudrate=self._baudrate,
              time_length=self._total_blinks,
              close_on_exit=self._close_on_exit)
