import csv
import re
from cityUF import patternUFs
from changeVars import updatedVars, lowerVars


def readCSV():
    data = []
    try:
        print('try')
        with open('Dados/2004exp.txt', 'r', newline='') as file:
            read = csv.reader(file, delimiter=';')
            for row in read:
                data.append(row)

    except:
        print('except')
        with open('Dados/2004exp.csv', 'r', newline='') as file:
            read = csv.reader(file)
            for row in read:
                data.append(row)

    keys = data[0]
    data.pop(0)
    return keys, data
    # deixa em letra minuscula as variaveis


def transformDict(keys, data1):
    arrayMap = []
    for array in (data1):
        map = {}
        for values in range(len(array)):
            map[keys[values]] = array[values]
        arrayMap.append(map)
    return arrayMap


def generateCode(arrayMaps):
    for index in range(len(arrayMaps)):
        dict = arrayMaps[index]
        dict['index'] = dict.get('nu_ano') + str(index)
    return arrayMaps


def contactAtributos(arrayMap):
    arrayMap = patternTurnos(arrayMap)
    return arrayMap


def patternTurnos(arrayMap):
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
            elif int(dict['co_turno_graduacao']) == 2:
                print(dict['co_turno_graduacao'])
                dict["varCursoTurnos"].update({'varCursoVespertino': True})
                del dict['co_turno_graduacao']
            elif int(dict['co_turno_graduacao']) == 3:
                dict["varCursoTurnos"].update({'varCursoIntegral': True})
                del dict['co_turno_graduacao']
            elif int(dict['co_turno_graduacao']) == 4:
                dict["varCursoTurnos"].update({'varCursoNoturno': True})
                del dict['co_turno_graduacao']
    return arrayMap


def formatQuestions_qe_i(arrayMap):
    # Formata atributos do questionario em uma dict só
    for dict in arrayMap:
        dict['qe_Questionario'] = {}
        i = 1
        for keys in list(dict.keys()):
            x = re.search('qe_i\d+', keys)
            if (x):
                chave = x.string
                if i < 10:
                    dict['qe_Questionario'].update(
                        {'qe_i' + '0' + str(i): dict[chave]}
                    )
                    del dict[keys]
                else:
                    dict['qe_Questionario'].update(
                        {'qe_i' + str(i): dict[chave]})
                    del dict[keys]
                i += 1

    return arrayMap


def formatQuestions_CO_RS(arrayMap):
    for dict in arrayMap:
        dict['rs_Questionario'] = {}
        i = 1
        for keys in list(dict.keys()):
            versao_qp = re.search('qp_i\d+', keys)
            versao_co_rs = re.search('co_rs_i\d+', keys)
            if (versao_qp):
                versao_qp = versao_qp.string
                dict['rs_Questionario'].update(
                    {' co_rs_i' + str(i): dict[versao_qp]}
                )
                del dict[keys]
                i += 1
            elif (versao_co_rs):
                versao_co_rs = versao_co_rs.string
                dict['rs_Questionario'].update(
                    {versao_co_rs: dict[versao_co_rs]}
                )
                del dict[keys]

    return arrayMap


def formatQuestions_nt_ce(arrayMap):
    global versao_co_rs
    for dict in arrayMap:
        dict['nt_ce_Questionario'] = {}
        for keys in list(dict.keys()):
            nt_ce = re.search('nt_ce_d\d+', keys)
            if nt_ce:
                nt_ce = nt_ce.string
                dict['nt_ce_Questionario'].update(
                    {keys: dict[nt_ce]}
                )
                del dict[keys]

    return arrayMap


def formatQuestions_tp_sce(arrayMap):
    global versao_co_rs
    for dict in arrayMap:
        dict['tp_sce_Questionario'] = {}
        for keys in list(dict.keys()):
            tp_sce_d = re.search('tp_sce_d\d+', keys)
            if tp_sce_d:
                tp_sce_d = tp_sce_d.string
                dict['tp_sce_Questionario'].update(
                    {keys: dict[tp_sce_d]}
                )
                del dict[keys]

    return arrayMap


def execute():
    keys, data = readCSV()

    keys = lowerVars(keys)
    keys = updatedVars(keys)
    enadeData = transformDict(keys, data)
    enadeData = contactAtributos(enadeData)
    enadeData = formatQuestions_qe_i(enadeData)
    enadeData = formatQuestions_CO_RS(enadeData)
    enadeData = formatQuestions_nt_ce(enadeData)
    enadeData = formatQuestions_tp_sce(enadeData)

    enadeData = generateCode(enadeData)
    enadeData = patternUFs(enadeData)
    return enadeData


print(execute())
