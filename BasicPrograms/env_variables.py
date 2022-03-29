'''
    @Author: Nishanth
    @Date: 29-03-2022 7:29:00
    @Last Modified by: Nishanth
    @Last Modified time: 29-03-2022 7:29:00
    @Title: get system environmet variables
'''

import logging
import os
import sys


def get_env_variables():
    """
        Description:
            lists all system environment variables
        
        Parameters:
            None
        
        Return:
            None
    """
    env_variables_as_string = ""
    for item in os.environ.items():
        env_variables_as_string += f"\n{item[0]}: {item[1]}"    
    logging.info(f"System env variables:{env_variables_as_string}")

if __name__ == '__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"basic_programs.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    get_env_variables()