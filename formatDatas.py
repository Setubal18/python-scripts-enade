import csv
import re


def readCSV():
    data = []
    new_keys = []
    arrayMap = []
    map = {}
    with open('Dados/2004exp.csv', 'r', newline='') as file:
        read = csv.reader(file)
        for row in read:
            data.append(row)

    # with open('Dados/2011exp.txt', 'r', newline='') as file:
    #     read = csv.reader(file, delimiter=';')
    #     for row in read:
    #         data.append(row)

    keys = data[0]
    data.pop(0)

    # deixa em letra minuscula as variaveis
    for i in range(len(keys)):
        new_key = keys[i].lower()
        keys.pop(i)
        keys.insert(i, new_key)

    # Transforma o array em um dict
    for array in (data):
        map = {}
        for values in range(len(array)):
            map[keys[values]] = array[values]
        arrayMap.append(map)

    # Transforma formata atributo do turno do curso
    for dict in (arrayMap):
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
        #print(dict)

    # Formata atributos do questionario em uma dict só
    for dict in arrayMap:
        dict['qeQuestionario'] = {}
        quest = []
        for keys in list(dict.keys()):
            x = re.search('qe_i\d+', keys)
            if (x):
                chave = x.string
                dict['qeQuestionario'].update({chave: dict[chave]})
                del dict[keys]
        print(dict)
# def change(dict):

readCSV()
