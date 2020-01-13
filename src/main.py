# Define Imports
import os
import sys
from lib import is_balance_sheet, is_income_statement, parse_csv, check_file


# Entry Point
def main():
    file_name = sys.argv[1]
    values = parse_csv(file_name)
    check_file(values)


main()
