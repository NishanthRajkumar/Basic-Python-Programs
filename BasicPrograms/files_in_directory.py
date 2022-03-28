'''
    @Author: Nishanth
    @Date: 28-03-2022 17:00:00
    @Last Modified by: Nishanth
    @Last Modified time: 28-03-2022 17:20:00
    @Title: List all files in a given  directory
'''
import logging
import os
import sys

def get_file_list(directory):
    """
        Description:
            Gets list of files in directory
        
        Parameter:
            Accepts directory path as string
        
        Return:
            List of file names
    """
    return os.listdir(directory)


if __name__ == '__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"basic_programs.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    logging.info(f"List of files in 'BasicPrograms': {get_file_list(r'BasicPrograms')}")