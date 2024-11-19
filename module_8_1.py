def add_everything_up(a, b):
    try:
        type(a) == float or int
        type(b) == str
        result = a + b
    except TypeError:
        result = str(a) + str(b)
    else:
        type(a) and type(b) == float or int
        result = round(result, 3)
    return result


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
