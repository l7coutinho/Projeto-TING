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
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
