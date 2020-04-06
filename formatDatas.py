import csv
import re
from changeVars import updatedVars, lowerVars


def readCSV():
    data = []
    try:
        with open('Dados/2018exp.txt', 'r', newline='') as file:
            read = csv.reader(file, delimiter=';')
            for row in read:
                data.append(row)

    except:
        with open('Dados/2004exp.csv', 'r', newline='') as file:
            read = csv.reader(file)
            for row in read:
                data.append(row)

    keys = data[0]
    data.pop(0)
    return keys, data
    # deixa em letra minuscula as variaveis


def transformDict(keys, data):
    arrayMap = []
    # Transforma o array em um dict
    for array in (data):
        map = {}
        for values in range(len(array)):
            map[keys[values]] = array[values]
        arrayMap.append(map)
    return arrayMap


def contactAtributos(arrayMap):
    for dict in arrayMap:
        dict["varCursoTurnos"] = {}
        if 'in_matut' in dict and 'in_vesper' in dict and 'in_noturno' in dict:
            if dict['in_matut'] == 1:
                dict["varCursoTurnos"].update({'varCursoMatutino': True})
                del dict['in_matut']
            else:
                dict["varCursoTurnos"].update({'varCursoMatutino': False})
                del dict['in_matut']

            if dict['in_vesper'] == 1:
                dict["varCursoTurnos"].update({'varCursoVespertino': True})
                del dict['in_vesper']
            else:
                dict["varCursoTurnos"].update({'varCursoVespertino': False})
                del dict['in_vesper']

            if dict['in_noturno'] == 1:
                dict["varCursoTurnos"].update({'varCursoNoturno': True})
                del dict['in_noturno']
            else:
                dict["varCursoTurnos"].update({'varCursoNoturno': False})
                del dict['in_noturno']

        if 'co_turno_graduacao' in dict:
            if int(dict['co_turno_graduacao']) == 1:
                print(dict['co_turno_graduacao'])
                dict["varCursoTurnos"].update({'varCursoMatutino': True})
                del dict['co_turno_graduacao']
            if int(dict['co_turno_graduacao']) == 2:
                print(dict['co_turno_graduacao'])
                dict["varCursoTurnos"].update({'varCursoVespertino': True})
                del dict['co_turno_graduacao']
            if int(dict['co_turno_graduacao']) == 3:
                dict["varCursoTurnos"].update({'varCursoIntegral': True})
                del dict['co_turno_graduacao']
            if int(dict['co_turno_graduacao']) == 4:
                dict["varCursoTurnos"].update({'varCursoNoturno': True})
                del dict['co_turno_graduacao']
    return arrayMap


def formatQuestions_qe_i(arrayMap):
    # Formata atributos do questionario em uma dict só
    for dict in arrayMap:
        dict['qeQuestionario'] = {}
        quest = []
        for keys in list(dict.keys()):
            x = re.search('qe_i\d+', keys)
            if (x):
                chave = x.string
                # endAtributo(chave)
                dict['qeQuestionario'].update({chave: dict[chave]})
                del dict[keys]
    return arrayMap


keys, data = readCSV()

keys = lowerVars(keys)
keys = updatedVars(keys)

arrayMap = transformDict(keys, data)
arrayMap = contactAtributos(arrayMap)
arrayMap = formatQuestions_qe_i(arrayMap)
print(arrayMap)
