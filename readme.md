# Salesforce Object Fields Comparator

A simple tool made to compare fields between multiple environments.

## How to use

Create a Excel workbook following the sample provided in the repository. Create sheets for each of your environments. In these sheets, label a column "Fields", and then input the fields (API names) of the object in this column (you can easily extract them using the Salesforce Dev Tools). **The workbook must contain a 'DEV' sheet, which will be used as a basis for comparison.**

Then, drag and drop your .xlsx file on the `comparator.py` script. The discrepancies between the environments will be stored in the `results.xlsx` file.
