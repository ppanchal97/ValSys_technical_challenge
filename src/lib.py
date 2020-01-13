# Define Imports
from collections import Counter
import csv
import re


# Checks if a given file is a balance sheet by computing if assets = (liabilities + equity)
def is_balance_sheet(data):
    x = value, count = Counter(data.values()).most_common(1)[0]
    for key, value in data.items():
        if value == x[0]:
            if "asset" in key.lower() or "liabilit" in key.lower():
                return True
    return False


# Check if a given file is an income statement by computing the net income and adjusting for deductibles
def is_income_statement(data):
    tax_figures = []
    nums = []
    for key, value in data.items():
        if "tax" in key.lower():
            if "income" in key.lower() or "provision" in key.lower() or "loss" in key.lower():
                nums.append(key)
                tax_figures.append(value)
    # check if values are immediately next to each other in accordance with GAAP principles
    if len(nums) == 2 and nums[1] == nums[0 + 1]:
        # calculate the total PNL
        net_income = tax_figures[0] - abs(tax_figures[1])
        for key, value in data.items():
            if value == net_income:
                return True
    return False


# Parse a CSV file into a dictionary containing key-value pairs. Hashmap values are standardized to type float
def parse_csv(file_path):
    with open(f'{file_path}') as csv_file:
        values = {}
        csv_reader = csv.reader(csv_file, delimiter=",")
        for date, key, value in csv_reader:
            # sanitize data
            if value != "" and value != "Value" and value != "0":
                pattern = '[$, £, \s, (, )]'
                val = re.match(pattern, value)
                if val:
                    # remove unwanted characters
                    x = re.sub('[$, £, \s, (, )]+', '', value).strip()
                    if key not in values.keys():
                        values[key] = float(x)
                else:
                    values[key] = float(value)
    return values


# Return the type of financial document
def check_file(data):
    if is_balance_sheet(data):
        print('Balance Sheet')
    elif is_income_statement(data):
        print('Income Statement')
    else:
        print('Cash-Flow Statement')


# Validate terminal user input
def check_args(args):
    if len(args) != 2:
        print("Incorrect number of arguments, Please check correct format")
        return False
    return True
