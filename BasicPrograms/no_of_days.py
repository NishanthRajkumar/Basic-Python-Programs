'''
    @Author: Nishanth
    @Date: 28-03-2022 17:00:00
    @Last Modified by: Nishanth
    @Last Modified time: 28-03-2022 17:00:00
    @Title: calculate number of days between two dates
'''
from datetime import date
import logging
import sys


def number_of_days(start_date, end_date):
        """
            Description:
                calculate number of days between two dates
            
            Parameter:
                accepts 2 parameters: Start-date and end-date as date type
            
            Return:
                None
        """
        if type(start_date) != date or type(end_date) != date:
            logging.error("Invalid type! arguments passed to method must be of date type")
            return None
        date_difference = end_date - start_date
        no_of_days = date_difference.days
        logging.info(f"Number of days between {start_date} and {end_date} is {no_of_days}")


if __name__ == '__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"basic_programs.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    number_of_days(date(2022, 1, 20), date(2022, 3, 28))