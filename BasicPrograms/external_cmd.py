'''
    @Author: Nishanth
    @Date: 28-03-2022 17:00:00
    @Last Modified by: Nishanth
    @Last Modified time: 28-03-2022 17:20:00
    @Title: execute external command
'''
import logging
import os
import sys

def external_cmd(command):
    """
        Description:
            calls an external command in Python.
        
        Parameter:
            Accepts command string
        
        Return:
            None
    """
    os.system(command)


if __name__ == '__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"basic_programs.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    external_cmd(r'calc')