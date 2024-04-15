def exists_word(word, instance):
    list = []

    for data in instance._data:
        obj_word = {
            "palavra": word,
            "arquivo": data["nome_do_arquivo"],
            "ocorrencias": [],
        }

        for line_number, line in enumerate(data["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                obj_word["ocorrencias"].append({"linha": line_number + 1})

        if len(obj_word["ocorrencias"]) > 0:
            list.append(obj_word)

    return list


def search_by_word(word, instance):
    list = []

    for data in instance._data:
        obj_word = {
            "palavra": word,
            "arquivo": data["nome_do_arquivo"],
            "ocorrencias": [],
        }
        for line_number, line in enumerate(data["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                obj_word["ocorrencias"].append(
                    {"linha": line_number + 1, "conteudo": line}
                )

        if len(obj_word["ocorrencias"]) > 0:
            list.append(obj_word)

    return list
