'''
    @Author: Nishanth
    @Date: 28-03-2022 17:00:00
    @Last Modified by: Nishanth
    @Last Modified time: 28-03-2022 17:00:00
    @Title: checks if the given item is present in the list or not
'''
import logging
import sys


def check_item_is_in_list(item, search_list):
        """
            Description:
                checks if the given item is present in the list or not
            
            Parameters:
                accepts 2 parameters.
                item -> the item to search for in the list.
                search_list -> the list to search through
            
            Return:
                None
        """
        if item in search_list:
            logging.info(f"{item} is present in {search_list}")
        else:
            logging.info(f"{item} is not present in {search_list}")


if __name__ == '__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"basic_programs.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    check_item_is_in_list(12, [13,5,7,12,3])