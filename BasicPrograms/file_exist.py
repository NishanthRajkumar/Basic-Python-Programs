'''
    @Author: Nishanth
    @Date: 28-03-2022 17:00:00
    @Last Modified by: Nishanth
    @Last Modified time: 28-03-2022 17:00:00
    @Title: Checks if the given file path name exists or not
'''
import logging
import os
import sys


def check_file_exist(file_path_name):
        """
            Description:
                Checks if the given file path name exists or not
            
            Parameter:
                file path as string
            
            Return:
                None
        """
        file_existence = os.path.isfile(file_path_name)
        logging.info(f"file {file_path_name} exist? {file_existence}")


if __name__ == '__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"basic_programs.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    check_file_exist(r'get_doc.py')