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

## Function Declarations

#### `is_balance_sheet()`

- Arguments - 1 : Hashmap of the key, values in a CSV file
- Purpose - To check if a file is a balance sheet
- Return - True or False
- Return Type - Boolean

#### `is_income_statement()`

- Arguments - 1 : Hashmap of the key, values in a CSV file
- Purpose - To check if a file is an income statement
- Return - True or False
- Return Type - Boolean

#### `parse_csv()`

- Arguments - 1 : CSV file
- Purpose - To retrieve the key value pairs of a CSV file
- Return - Keys and values in the file
- Return Type - Hashmap (Dictionary)

#### `check_file()`

- Arguments - 1 : Hashmap of the key, values in a CSV file
- Purpose - To print the type of financial statement
- Return - Outputs to terminal type of file
- Return Type - /

#### `validate_args()`

- Arguments - 1 : Array of strings
- Purpose - To validate if the user has entered valid command line arguments
- Return - True or False
- Return Type - Boolean

## Explanation

- The categorisation algorithm has been implemented using basic theories and notions of accounting in accordance with the Generally Accepted Accounting Principles (GAAP). Each section lists the accounting principle, its explanation and the implementation logic. The process of accounts reconciliation (AR) has been carried out at the necessary steps to categorise the type of financial statement
- As the financial wordings in the keys of the CSV files might differ greatly between the accounting practices of various companies, reliance is placed on the values. Validation of the characters in the keys occurs at the secondary level.

### Balance Sheet

- A balance sheet is a financial statement that reports a company's assets, liabilities and shareholders' equity at a specific point in time, and provides a basis for computing rates of return and evaluating its [capital structure](https://www.investopedia.com/terms/c/capitalstructure.asp). It is a financial statement that provides a snapshot of what a company owns and owes, as well as the amount invested by shareholders.
- A fundamental principle of a balance sheet is that

`Assets = (Liabilities + Equity)`

As the GAAP principles state that Total Assets must be declared in addition to the Total liabilities and shareholders' equity, we can expect that that two values in the balance sheet must be equivalent to each other. Firstly, This can be tested using the equality operator (==). If the function finds that there are two keys with similar values, it carries out the second level of validation. The keys themselves are checked to verify if they contain the word "asset" or "liabilit". This is to ensure that there is reasonable support for words such as "assets", "liability" and "liabilities"

### Income Statement

- An income statement is one of the three important [financial statements](https://www.investopedia.com/terms/f/financial-statements.asp) used for reporting a company's financial performance. Also known as the [profit and loss statement](https://www.investopedia.com/terms/p/plstatement.asp) or the statement of revenue and expense, the income statement primarily focuses on the [company’s revenues and expenses](https://www.investopedia.com/ask/answers/070915/how-do-you-calculate-company-equity.asp) during a particular period.
- As all companies have to pay corporation tax, the gross and net amounts of income have to be declared in the income statement. According to the GAAP principles, the income statement must declare an income (either a profit or a loss) in addition to declaring the deductibles immediately below.
- The function iterates through the keys of the CSV file to find keys that contain the string "tax". If a match is found, further validation is carrier out by checking if the key also contains the strings "income" or "provision" or "loss" to confirm that the value of the key is indeed the net income of the company.
- As the GAAP principles state that any deductibles from the net income of a company must be declared immediately below, the function uses the index position of the keys that fulfil the above requirement to judge whether they are adjacent. If the two keys are adjacent, then the values of these keys can be used to compute the net income or loss of the company.
- The second level of validation occurs when the function if the net income figure devised from the above steps is present in the income statement.

### Cash Flow Statement

- The statement of cash flows, or the cash flow statement, is a financial statement that summarises the amount of [cash and cash equivalents](https://www.investopedia.com/terms/c/cashandcashequivalents.asp) entering and leaving a company. The cash flow statement (CFS) measures how well a company manages its cash position, meaning how well the company generates cash to pay its debt obligations and fund its operating expenses.
- As the program will only be used with financial statements, of which there are only 3. If it recognises that a file is not an Income Statement or a Balance Sheet, it must be of the type Cash Flow Statement.

### Known Issues

- The Starbucks Income statement file in sample_data/starbucks.csv return an error

```
  File "main.py", line 15, in <module>
  main()
  File "main.py", line 11, in main
  csv_values = parse_csv(file_name)
  File "/Users/parik/Desktop/ValSys/src/lib.py", line 41, in parse_csv
  for date, key, value in csv_reader:
  ValueError: not enough values to unpack (expected 3, got 2)
```
