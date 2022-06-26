'''
    @Author: Nishanth
    @Date: 28-03-2022 17:00:00
    @Last Modified by: Nishanth
    @Last Modified time: 28-03-2022 17:00:00
    @Title: To displays the doc string of the given method
'''
import logging
import sys


def get_doc(method):
        """
            Description:
                displays the doc string of the given method
                
            Parameters:
                None
            
            Return:
                None
        """
        logging.info(method.__doc__)

if __name__ == '__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"basic_programs.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    get_doc(get_doc)