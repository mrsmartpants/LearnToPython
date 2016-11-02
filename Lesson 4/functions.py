

def isfloat(str_val):
    try:
        float(str_val)
        return True
    except ValueError:
        return False
print("Is pi a float ?", isfloat("Pi"))