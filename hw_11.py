# Will you make it?


def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump > mpg * fuel_left:
        return False
    else:
        return True


# Will there be enough space?


def enough(cap, on, wait):
    if on + wait > cap:
        cant = (wait + on) - cap
        return cant
    else:
        return 0


# Are You Playing Banjo?


def areYouPlayingBanjo(name):
    for s in name:
        if s == "R":
            z = (" plays banjo")
            break
        elif s == "r":
            z = (" plays banjo")
            break
        else:
            z = " does not play banjo"
            break

    return name + z


# Convert boolean values to strings 'Yes' or 'No'.


def bool_to_word(boolean):
    if boolean == True:
        Str = "Yes"
    else:
        Str = "No"
    return Str


# Counting sheep...


def count_sheeps(sheep):
    z = 0
    m = False
    for s in sheep:
        if s == True:
            z += 1
    return z


# Is this my tail?


def correct_tail(body, tail):
    sub = len(body)
    last = body[sub - 1]
    if last == tail:
        return True
    else:
        return False
