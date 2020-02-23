def filter_words(st):
    """
    Write a function taking in a string like WOW this is REALLY amazing and returning Wow this is really amazing.
     String should be capitalized and properly spaced. Using re and string is not allowed.
    """
    last = (len(st)) - 1
    stlist = []

    for s in st:
        stlist.append(s)
    if stlist[0] == ' ':
        del stlist[0]
    if stlist[last] == ' ':
        del stlist[last]
    sm = ''.join(stlist)
    sm = sm.replace('   ', ' ')
    sm = sm.replace('  ', ' ')
    return sm.capitalize()
