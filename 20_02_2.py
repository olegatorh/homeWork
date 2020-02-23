def list_animals(animals):
    """Fix the loop!"""
    slist = ''
    for i in range(len(animals)):
        slist += "{0}. {1}\n".format(i + 1, animals[i])
    return slist