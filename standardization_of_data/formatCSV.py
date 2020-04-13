import csv

import xlrd


def readPlan(arq1):
    data = []
    print(arq1)
    book = xlrd.open_workbook(arq1)
    plan = book.sheets()
    print(plan)
    for i in range(plan[0].nrows):
        print(plan[0].row_values(i))
        data.append(plan[0].row_values(i))
    print(data)
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
    columnDescription = ''
    columnAttribute = ''
    for attribute in range(len(column)):
        print(column[attribute])

        if len(column) == 5:
            print(column[attribute])
            columnVariable = column[0]
            if attribute == 4:
                if eVazio(column[attribute], attribute) or column[attribute] == '-':
                    columnAttribute = 'Não Consta/Faltando'
                else:
                    columnAttribute = column[attribute]
            if attribute == 3:
                if eVazio(column[attribute], attribute) or column[attribute] == '-':
                    columnDescription = 'Não Consta/Faltando'
                else:
                    columnDescription = column[attribute]

        if len(column) == 6:
            columnVariable = column[1]
            if attribute == 5:
                if eVazio(column[attribute], attribute) or column[attribute] == '-':
                    columnAttribute = 'Não Consta/Faltando'
                else:
                    columnAttribute = column[attribute]
            if attribute == 4:
                if eVazio(column[attribute], attribute) or column[attribute] == '-':
                    columnDescription = 'Não Consta/Faltando'
                else:
                    columnDescription = column[attribute]

    if columnAttribute != '' and columnAttribute != '' and columnDescription != '':
        return [columnVariable, columnAttribute, columnDescription]


def formatRow(**sheets):
    newSheets = []
    if len(sheets) == 1:
        for row in sheets["sheet"]:
            nova_row = formtCollum(row)

            if nova_row:
                newSheets.append(nova_row)
        print(newSheets)
        return newSheets

    # Futura Implementação
    # else:
    #     for index in range(len(sheets["oldsheet"])):
    #         try:
    #             nova_row = addcolumn(sheets["oldsheet"][index], formatRow(sheet=sheets["sheet"])[index])
    #         except IndexError:
    #             if len(sheets["oldsheet"]) > len(sheets["sheet"]):
    #                 nova_row = sheets["oldsheet"][index]
    #                 for i in range(len(sheets["sheet"][index])):
    #                     nova_row.extend('')
    #             if len(sheets["oldsheet"]) < len(sheets["sheet"]):
    #                 for i in range(len(sheets["oldsheet"][index])):
    #                     if i <= len(sheets["oldsheet"][index]):
    #                         nova_row.insert(i, '')
    #                     else:
    #                         nova_row.extend(formtCollum(sheet=sheets["sheet"])[index])
    #
    #         if nova_row:
    #             newSheets.append(nova_row)
    #     return newSheets


def addcolumn(oldColumn, column):
    oldColumn.extend([column])
    return oldColumn


def createCSV(newSheets,ano):
    newSheets.insert(0, ['', ano, ''])
    with open('Variaveis dos Dados/'+ano+'variaveis.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(newSheets)
    print("Sucesso ao Criar Arquivo !")


def alteredCSV(newSheets):
    with open('Variaveis dos Dados/variaveis.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(newSheets)
    print("Sucesso ao Editar Arquivo !")


def readCSV():
    oldest = []
    with open('Variaveis dos Dados/variaveis.csv', 'r', newline='') as file:
        read = csv.reader(file)
        print(read)
        for row in read:
            print(row)
            oldest.extend([row])
        return oldest


def manipulatecsv(sheet,ano):
        createCSV(formatRow(sheet=sheet),ano)
    # except:
    #     oldSheet = readCSV()
    #     alteredCSV(formatRow(oldsheet=oldSheet, sheet=sheet))

args = input('Coloque o caminho da planilha : ')
ano = input('Ano da  planilha:')
manipulatecsv(readPlan(args), str(ano))

