#!/usr/bin/python3

import openpyxl

__version__ = '1.0.0'


def readexcel():
    wb = openpyxl.load_workbook(filename="efatura.xlsx", read_only=True)
    ws = wb.get_sheet_by_name('EFatura')

    listofdata = []

    for row in ws.rows:
        listofdata.append(dict(Random=row[0].value, Name=row[1].value))

    return listofdata


if __name__ == '__main__':
    readexcel()
