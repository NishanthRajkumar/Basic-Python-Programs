import logging
import sys


def first_last_from_list():
        """
            Description:
                display first and last item of the list
                
            Parameters:
                None
            
            Return:
                None
        """
        color_list = ["Red","Green","White" ,"Black"]
        logging.info(f"First color: {color_list[0]}; Last color: {color_list[-1]}")


if __name__ == '__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"basic_programs.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    first_last_from_list()