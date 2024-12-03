def find_common_participants(names1, names2, separator=','):
    names1, names2 = [i for i in names1.split(separator)], [i for i in names2.split(separator)]
    return sorted([i for i in names1 if i in names2])
