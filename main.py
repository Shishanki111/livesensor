from sensor.exception import SensorException
import os
import sys

def test_exception():
    try:
        a=1/0
    except Exception as e:
        # raise SensorException(e,sys)
        raise e


if __name__ == "__main__": # use for prevent excution on import
    try:
        test_exception()
    except Exception as e:
        print(e)