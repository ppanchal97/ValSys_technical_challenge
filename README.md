## Technical test


**Background:** We ingest a large amount of data across many different companies and time periods. One of the first challenges you face when trying to organise large chunks of files is identifying the main components. In financial statements, the 3 main file types are the income statement, balance sheet and cash flow statement. Each of these (typically) have unique properties.


**The challenge:** Write a program that allows you to categorise the different types of statements found in the sample data folder. The three child folders (income statement, balance sheet, cash flow statement) are the statement types your program will need to identify. The format is "/sample_data/statement_type/company_filing.csv". Once completed, your program should be able to identify an unseen company's filing by stating whether it is an income statement, balance sheet or cash flow statement. Each of the folders in /sample_data contain example files which you will need to analyse in order to identify the differences between the file types; rely on anything you can think of to try and identify the filings (short of matching the file path)! The challenge should be written either in Python or Golang.


**What we’ll be assessing:**

- Functionality - does it work?

- File structure and design patterns

- Data structures

- Dependencies

## Submitting
When you're ready to submit, upload the repository to a code hosting service like Github or Bitbucket and share it with us!