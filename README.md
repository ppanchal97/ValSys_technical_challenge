## Financial Statement Checker

Implement a program that categorises a file by a financial statement type, per the below.

    $ python3 main.py /Users/parik/Desktop/ValSys/sample_data/income_statement/chipotle.csv
    Income Statement

## Files

1.  Main.py

- Contains the entry point for the file

2.  Lib.py

- Exports functions for categorising financial statements, validating arguments and parsing CSV files

## Usage

- argv[0] : main file (main.py)
- argv[1] : relative or absolute path to CSV file

      	 `python3 main.py PATH_TO_FILE`


## Explanation

- The categorisation algorithm has been implemented using basic theories and notions of accounting in accordance with the Generally Accepted Accounting Principles (GAAP). Each section lists the accounting principle, its explanation and the implementation logic.

### Balance Sheet

- A balance sheet is a financial statement that reports a company's assets, liabilities and shareholders' equity at a specific point in time, and provides a basis for computing rates of return and evaluating its [capital structure](https://www.investopedia.com/terms/c/capitalstructure.asp). It is a financial statement that provides a snapshot of what a company owns and owes, as well as the amount invested by shareholders.
