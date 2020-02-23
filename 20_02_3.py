def double_char(s):
    """double_char("String") ==> "SSttrriinngg"

double_char("Hello World") ==> "HHeelllloo  WWoorrlldd"

double_char("1234!_ ") ==> 11223344!!__  """
    new_s = ""
    for i in s:
        new_s += i * 2
    return new_s