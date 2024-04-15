import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    list = txt_importer(path_file)

    for index in instance._data:
        if index['nome_do_arquivo'] == path_file:
            return

    file = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(list),
        'linhas_do_arquivo': list
    }

    instance.enqueue(file)
    print(file, file=sys.stdout)


def remove(instance):
    if len(instance._data) == 0:
        print("Não há elementos", file=sys.stdout)
        return
    path_file = instance.dequeue()['nome_do_arquivo']
    print(f'Arquivo {path_file} removido com sucesso', file=sys.stdout)


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        print(file, file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
