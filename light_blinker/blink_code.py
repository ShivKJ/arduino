from getpass import getuser
from sys import maxsize

from serial import Serial
from serial.serialutil import SerialException
from time import sleep

ZERO = '0'.encode()
ONE = '1'.encode()


def blink(port, func, time_length=None, start_with_on=True):
    """
    function to make led light.

    :param port:
    :param func:
    :param time_length:
    :param start_with_on:
    :return:
    """
    try:
        device = Serial(port, 9600)
    except SerialException as e:
        print('Check: sudo chown {} {}'.format(getuser(), port))
        raise e
    else:

        if time_length is None:
            time_length = maxsize

        status = start_with_on

        if status is True:
            device.write(ONE)
        else:
            device.write(ZERO)

        for t in range(time_length):
            sleep(func(t))

            if status is True:
                device.write(ZERO)
                status = False
            else:
                device.write(ONE)
                status = True

        device.close()
