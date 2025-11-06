import openpyxl

def get_data(sheet_name):
    workbook = openpyxl.load_workbook("test_data/test_data.xlsx")
    sheet = workbook[sheet_name]
    data = []
    for row in sheet.iter_rows(min_row=2,values_only=True):
        data.append(row)
    return data # Skip header row