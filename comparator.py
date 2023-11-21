import sys
import os
from pandas import *

file = sys.argv[1];

def load_excel_file_as_dataframe(file):
    try:
        if os.path.isfile(file):
            excel_workbook = read_excel(file, sheet_name=None);
            if ('DEV' not in list(excel_workbook.keys())):
                raise ValueError;
            return excel_workbook;
        else:
            raise ValueError;
    except ValueError:
        print("The provided Excel Dataframe does not meet the requirements for object fields comparison (see sample file).");

try:
    if file == None:
        raise ValueError;
    if file[len(file) - 4:] != 'xlsx':
        raise ValueError;
    workbook = load_excel_file_as_dataframe(file);
    dev_sheet_list = workbook.get('DEV')['Fields'].to_list();
    fields_only_present_in_dev = [];
    for sheet_name, sheet_content in workbook.items():
        if sheet_name != 'DEV':
            for field in dev_sheet_list:
                if (field not in sheet_content['Fields'].to_list()) and (field not in fields_only_present_in_dev):
                    fields_only_present_in_dev.append(field);
    returned_dataframe = DataFrame(fields_only_present_in_dev, columns=['Fields only present in DEV']).to_excel('./result.xlsx');
except ValueError:
    print("Please provide a valid .xlsx file.");