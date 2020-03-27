import xlrd
import csv


def readPlan(arq1):
    data = []
    book = xlrd.open_workbook(arq1)
    plan = book.sheets()

    for i in range(plan[0].nrows):
        data.append(plan[0].row_values(i))

    return data


def eVazio(value, position):
    if value == '' and position == 1:
        return True
    if value == '' and position == 5:
        return True
    if value == '' and position == 4:
        return True


def formtCollum(column):
    columnVariable = ''
    columnAttribute = ''
    for attribute in range(len(column)):
        if eVazio(column[attribute], attribute) and eVazio(column[attribute], attribute):
            break
        else:
            if attribute == 1:
                columnVariable = column[attribute]
            if attribute == 5:
                if column[attribute] == '' or column[attribute] == '-':
                    columnAttribute = column[attribute - 1]
                else:
                    columnAttribute = column[attribute]
            if attribute == 4 and not columnAttribute:
                columnAttribute = column[attribute]
            if columnAttribute != '' and columnAttribute != '':
                return [columnVariable, columnAttribute]


def formatRow(sheets):
    newSheets = []

    for row in sheets:
        nova_row = formtCollum(row)
        if nova_row:
            newSheets.append(nova_row)
    return newSheets


def writeCSV(newSheets):
    with open('Variaveis dos Dados/variaveis.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(newSheets)
    print("Success !")


arq = "Variaveis dos Dados/var2004.xls"

writeCSV(formatRow(readPlan(arq)))
