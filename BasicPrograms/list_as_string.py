'''
    @Author: Nishanth
    @Date: 28-03-2022 17:00:00
    @Last Modified by: Nishanth
    @Last Modified time: 28-03-2022 17:00:00
    @Title: Concatenates all elements in a list into a string and returns it
'''
import logging
import sys


def get_list_as_string(list_input):
        """
            Description:
                Concatenates all elements in a list into a string and returns it
            
            Parameters:
                accepts any list
            
            Return:
                returns a string
        """
        list_as_string = ""
        for item in list_input:
            list_as_string += item.__str__()
            list_as_string += ", "
        if len(list_as_string) > 2:
            list_as_string = list_as_string[:-2]
        return list_as_string


if __name__ == '__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"basic_programs.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    logging.info(get_list_as_string([True, 7, 9, 8.0, 3 + 9j]))