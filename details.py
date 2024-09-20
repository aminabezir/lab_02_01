def coefficient_by_part(part):
    k = 0
    if (part == 1 or part == 4 or part == 5):
        k = 1
    elif (part == 2):
        k = 1.2
    elif (part == 3 or part == 6):
        k = 1.1
    return k