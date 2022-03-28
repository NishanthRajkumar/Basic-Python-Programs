import logging
import sys

def name_reverse():
        """
            Description:
                gets first & last name from user. Prints the reverse of the full name
            
            Parameters:
                None
            
            Return:
                None
        """
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        full_name = first_name + " " + last_name
        logging.info("Reverse name: " + full_name[::-1])


if __name__ == '__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"basic_programs.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    name_reverse()