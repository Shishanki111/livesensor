from sensor.exception import SensorException
import os
import sys

from sensor.logger import logging


def test_exception():
    try:
        logging.info("getting error")
        a=1/0
    except Exception as e:
        raise SensorException(e,sys)
        # raise e #only give output(division by zero)


if __name__ == "__main__": # use for prevent excution on import
    try:
        test_exception()
    except Exception as e:
        print(e)