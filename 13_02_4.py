def create_array(n):
    """
Oh no, Timmy's created an infinite loop! Help Timmy find and fix the bug in his unfinished For Loop!
"""
    res = []
    i = 1

    while i <= n:
        res.append(i)
        i += 1
    return res
