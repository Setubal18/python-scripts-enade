from database import create_many, create_one
from standardization_of_data import execute


def main():
    path = input('Digite o caminho do arquivo :')
    choose = input('Deseja cadastrar varios de uma vez? (y/n)')
    dados = execute(path)
    print('Tamanho dos dados:', dados)
    if choose.lower() == 'n':
        create_one(dados)
    elif choose.lower() == 'y':
        create_many(dados)


i = 'y'
while i.lower() == 'n':
    main()
    print('Deseja salvar outro arquivo?(y = sim n = não)')
    i = input('(y/n) = ')
