# Define Imports
import os
import sys
from lib import is_balance_sheet, is_income_statement, parse_csv, check_file, validate_args


# Entry Point
def main():
    if validate_args(sys.argv):
        file_name = sys.argv[1]
        csv_values = parse_csv(file_name)
        check_file(csv_values)


main()
