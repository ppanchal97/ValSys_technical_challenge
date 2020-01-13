from collections import Counter
import csv
import re


# accepts key-value pairs and checks if it is a balance sheet or not
def is_balance_sheet(data):
    # find most frequently occuring value
    x = value, count = Counter(data.values()).most_common(1)[0]
    # print(x)
    # look at the key of that value to check if they contain assets or liabilities
    for key, value in data.items():
        if value == x[0]:
            if "asset" in key.lower() or "liabilit" in key.lower():
                # print(key, value)
                return True
    return False


def is_income_statement(data):
    # initialize constants
    tax_figures = []
    nums = []
    # find the word 'tax'
    for key, value in data.items():
        if "tax" in key.lower():
            if "income" in key.lower() or "provision" in key.lower() or "loss" in key.lower():
                # print(list(data).index(key))
                nums.append(key)
                tax_figures.append(value)
    # check if values are immediately next to each other according to GAAP
    if len(nums) == 2 and nums[1] == nums[0 + 1]:
        # print('adjacent')
        # calculate the total PNL
        net_income = tax_figures[0] - abs(tax_figures[1])
        # print(net_income)
        # # check if the value exists in the data now
        for key, value in data.items():
            if value == net_income:
                return True
    return False


def parse_csv(file_path):
    # Open and parse CSV
    with open(f'{file_path}') as csv_file:
        # define constants
        values = {}
        csv_reader = csv.reader(csv_file, delimiter=",")
        # insert key-value pairs into hashmap
        for date, key, value in csv_reader:
            # sanitize data
            # if fields are not empty or contain unwanted characters
            if value != "" and value != "Value" and value != "0":
                # specify the characters to remove
                pattern = '[$, £, \s, (, )]'
                val = re.match(pattern, value)
                # if you find a field that contains the specified character/s
                if val:
                    # replace the specified characters with empty space
                    x = re.sub('[$, £, \s, (, )]+', '', value).strip()
                    # insert it into the list
                    if key not in values.keys():
                        # convert to float to make easier to deal with
                        values[key] = float(x)
                else:
                        # convert to float and push
                    values[key] = float(value)
    return values


def check_file(data):
    if is_balance_sheet(data):
        print('is balance sheet')
    elif is_income_statement(data):
        print('is income statement')
    else:
        print('is cash-flow statement')
