'''
    @Author: Nishanth
    @Date: 28-03-2022 17:00:00
    @Last Modified by: Nishanth
    @Last Modified time: 28-03-2022 17:00:00
    @Title: Print calendar given month and year
'''
from calendar import Calendar
import logging
import sys


def print_calendar(month, year):
        """
            Description:
                prints calendar for given month and year
            
            Parameter:
                accepts 2 arguments. Month and year as integers
            
            Return:
                None
        """
        mycalendar = Calendar()
        result = mycalendar.monthdatescalendar(year, month)
        logging.info(f"Calendar for {month}, {year}:\n{result}")


if __name__ == '__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"basic_programs.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    print_calendar(3, 2022)