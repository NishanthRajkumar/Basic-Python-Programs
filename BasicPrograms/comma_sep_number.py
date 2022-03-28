'''
    @Author: Nishanth
    @Date: 28-03-2022 17:00:00
    @Last Modified by: Nishanth
    @Last Modified time: 28-03-2022 17:00:00
    @Title: Generate a list and a tuple using comma separated numbers
'''
import logging
import sys

def comma_sep_numbers():
        """
            Description:
                accepts a sequence of comma-separated numbers from user.
                Generate a list and a tuple with those numbers
                
            Parameters:
                None
            
            Return:
                None
        """
        user_input = input("Enter multiple nos seperated by ',': ")
        number_list = list(map(int, user_input.split(',')))
        number_tuple = tuple(number_list)
        logging.info(f"Number list: {number_list}")
        logging.info(f"Number tuple: {number_tuple}")


if __name__ == '__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"basic_programs.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    comma_sep_numbers()