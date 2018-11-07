from getpass import getuser
from sys import maxsize

from serial import Serial
from serial.serialutil import SerialException
from time import sleep

ZERO = '0'.encode()
ONE = '1'.encode()

ON = True
OFF = False


def blink(port, func, baudrate=9600, time_length=None, close_on_exit=False):
    """
    function to make led light.

    :param port:
    :param func:
    :param baudrate:
    :param time_length:
    :param close_on_exit:
    :return:
    """
    try:
        device = Serial(port, baudrate=baudrate)
    except SerialException as e:
        print('Check: sudo chown {} {}'.format(getuser(), port))
        raise e
    else:
        if time_length is None:
            time_length = maxsize

        # Setting 'status' to OFF so that it will be turn on in first iteration.
        status = OFF

        for t in range(time_length):
            if status is ON:
                # as 'status' is ON so turning off the light and updating 'statue' to OFF
                device.write(ZERO)
                status = OFF
            else:
                # as 'status' is OFF so turning on the light and updating 'status' to ON
                device.write(ONE)
                status = ON

            sleep(func(t))

        if close_on_exit is True:
            device.write(ZERO)

        device.close()
