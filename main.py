from database import create
from standardization_of_data import execute


def main():
    path = input('Digite o caminho do arquivo :')
    dados = execute(path)
    for dict in dados:
        create(dict)


i = 1
while i != 0:
    main()
    print('Deseja salvar outro arquivo?(1 = sim 0 = não)')
    i = input('(1/0) = ')
