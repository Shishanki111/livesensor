import sys
import os

def error_message_detail(error ,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    

# this is superclass all exception work under this class
class SensorException(Exception): #inherit exception
    def __init__(self, error_message, error_details:sys): # here sys used for capturing error
        super().__init__(error_message)
        
    def __str__(self): #dender fun
        return self.error_message