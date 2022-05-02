def thesaurus(*names):
    name_dict = dict()
    for el in sorted(names):
        key = el[0]
        if name_dict.get(key) is None:
            name_dict[key] = [el]
        else:
            name_dict[key].append(el)
    return name_dict



print(thesaurus('Виктор', 'Николай', 'Юлия', 'Анна', 'Иван'))