'''
    @Author: Nishanth
    @Date: 28-03-2022 17:00:00
    @Last Modified by: Nishanth
    @Last Modified time: 28-03-2022 17:00:00
    @Title: Prints out a set containing all the colors from color_list_1 which are not present in color_list_2
'''
import logging
import sys


def color_set_difference(color_list1, color_list2):
        """
            Description:
                Prints out a set containing all the colors from color_list_1 which are not present in color_list_2.
            
            Parameters:
                2 set type data containing list of colors

            Return:
                None
        """
        if type(color_list1) != set or type(color_list2) != set:
            logging.error("The input parameter is not a set")
            return None
        logging.info(f"The colors from {color_list1} not in {color_list2} are: {color_list1 - color_list2}")

if __name__ == '__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"basic_programs.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    color_set_difference(set(["White", "Black", "Red"]), set(["Red", "Green"]))