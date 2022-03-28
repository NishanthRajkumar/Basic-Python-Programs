'''
    @Author: Nishanth
    @Date: 28-03-2022 17:00:00
    @Last Modified by: Nishanth
    @Last Modified time: 28-03-2022 17:00:00
    @Title: Get CPU count
'''
import logging
import os
import sys

def get_cpu_count():
    """
            Description:
                Gets cpu count
            
            Parameter:
                None
            
            Return:
                None
    """
    logging.info(f"CPU count: {os.cpu_count()}")


if __name__ == '__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"basic_programs.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    get_cpu_count(r'get_doc.py')