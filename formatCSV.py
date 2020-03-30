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
            if not column[attribute] == '' and attribute <= 1 and not columnVariable:
                columnVariable = column[attribute]

            if attribute == 5:
                if column[attribute] == '' or column[attribute] == '-':
                    columnAttribute = column[attribute - 1]
                else:
                    columnAttribute = column[attribute]

            if attribute == 3 and not columnAttribute:
                if column[attribute] != '' or column[attribute] != '-':
                    if column[attribute + 1] == '' or column[attribute + 1] == '-':
                        columnAttribute = column[attribute]
                    else:
                        columnAttribute = column[attribute + 1]

            if columnAttribute != '' and columnAttribute != '':
                return [columnVariable, columnAttribute]


def formatRow(**sheets):
    newSheets = []
    if len(sheets) == 1:
        for row in sheets["sheet"]:
            nova_row = formtCollum(row)
            if nova_row:
                newSheets.append(nova_row)
        return newSheets

    else:
        for index in range(len(sheets["oldsheet"])):
            try:
                nova_row = addcolumn(sheets["oldsheet"][index], formatRow(sheet=sheets["sheet"])[index])
            except IndexError:
                if len(sheets["oldsheet"]) > len(sheets["sheet"]):
                    nova_row = sheets["oldsheet"][index]
                    for i in range(len(sheets["sheet"][index])):
                        nova_row.extend('')
                if len(sheets["oldsheet"]) < len(sheets["sheet"]):
                    for i in range(len(sheets["oldsheet"][index])):
                        if i <= len(sheets["oldsheet"][index]):
                            nova_row.insert(i, '')
                        else:
                            nova_row.extend(formtCollum(sheet=sheets["sheet"])[index])

            if nova_row:
                newSheets.append(nova_row)
        return newSheets


def addcolumn(oldColumn, column):
    oldColumn.extend([column])
    return oldColumn


def createCSV(newSheets):
    newSheets.insert(0, ['', ''])
    with open('Variaveis dos Dados/variaveis.csv', 'w', newline='') as file:
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


def manipulatecsv(sheet):
    try:
        createCSV(formatRow(sheet=sheet))
    except:
        oldSheet = readCSV()
        alteredCSV(formatRow(oldsheet=oldSheet, sheet=sheet))


arqs = [
    'C:/Users/setub/Documents/CEULP/PROICT/Dados/microdados_enade_2010/1.LEIA-ME/2010.xls',
    'C:/Users/setub/Documents/CEULP/PROICT/Dados/microdados_enade_2011/1.LEIA-ME/Dicionário de variáveis dos '
    'Microdados do Enade_Edição 2011.xls',
    'C:/Users/setub/Documents/CEULP/PROICT/Dados/microdados_enade_2012/1.LEIA-ME/Dicionário de variáveis dos '
    'Microdados do Enade_Edição 2012.xls',
    'C:/Users/setub/Documents/CEULP/PROICT/Dados/microdados_enade_2013/1.LEIA-ME/Dicionário de variáveis dos '
    'Microdados do Enade_Edição 2013.xls',
    'C:/Users/setub/Documents/CEULP/PROICT/Dados/microdados_enade_2014/1.LEIA-ME/Dicionário de variáveis dos '
    'Microdados do Enade_Edição 2014.xls',
    'C:/Users/setub/Documents/CEULP/PROICT/Dados/microdados_enade_2015/1.LEIA-ME/Dicionário de variáveis dos '
    'Microdados do Enade_Edição 2015.xls',
    'C:/Users/setub/Documents/CEULP/PROICT/Dados/microdados_enade_2016_versao_28052018/microdados_enade2016/1'
    '.LEIA-ME/Dicionário de variáveis dos Microdados do Enade_Edição 2016.xls',
    'C:/Users/setub/Documents/CEULP/PROICT/Dados/microdados_enade_2017/1.LEIA-ME/Dicionário de variáveis dos '
    'Microdados do Enade_Edição 2017.xls',
    'C:/Users/setub/Documents/CEULP/PROICT/Dados/microdados_enade_2018/1.LEIA-ME/Dicionário de variáveis dos '
    'Microdados do Enade_Edição 2018.xls']

args = input('Coloque o caminho da planilha : ')
manipulatecsv(readPlan(args))
# alteredCSV()
