'''
    @Author: Nishanth
    @Date: 28-03-2022 17:00:00
    @Last Modified by: Nishanth
    @Last Modified time: 28-03-2022 17:00:00
    @Title: create a histogram from the given list of integers
'''
import logging
import sys


def plot_histogram(list_of_int):
        """
            Description:
                creates a histogram from the given list of integers.
                The histogram is displayed using '*'
            
            Parameters:
                None
            
            Return:
                None
        """
        histogram_string = ""
        for item in list_of_int:
            if type(item) != int:
                logging.error("Invalid list item! must be int")
                return None
            if item < 0:
                logging.error("Invalid list item! the int must be > 0")
                return None
            for _ in range(item):
                histogram_string += "*"
            else:
                histogram_string += "\n"
        logging.info(f"Histogram for {list_of_int}:\n{histogram_string}")


if __name__ == '__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"basic_programs.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    plot_histogram([13,5,7,12,3])