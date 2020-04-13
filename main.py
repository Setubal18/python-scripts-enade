from database import create_many
from standardization_of_data import execute


def main():
    path = input('Digite o caminho do arquivo :')
    dados = execute(path)
    print('Tamanho dos dados:', )
    number = 0
    create_many(dados)
    # for dict in dados:
    #     create_one(dict)
    #     number = number + 1
    #     print('Já foi', number, ' Faltam :', str(len(dados) - number))


i = 1
while i != 0:
    main()
    print('Deseja salvar outro arquivo?(1 = sim 0 = não)')
    i = input('(1/0) = ')
