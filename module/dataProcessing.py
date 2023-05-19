def nameClass(number, result):
    if int(number[0]) < 0:
        return f"VALUE ERROS. IP is not valid, try again "

    elif int(number[0]) >= 0 and int(number[0]) <= 127:
        result = 'A'
    elif int(number[0]) > 127 and int(number[0]) <= 191:
        result = 'B'
    elif int(number[0]) >= 192 and int(number[0]) <= 223:
        result = 'C'
    elif int(number[0]) >= 224 and int(number[0]) <= 239:
        result = 'D'
    elif int(number[0]) > 239 and int(number[0]) <= 255:
        result = 'E'
    else:
        return f'The ip of {number} is no correponding class'
    return result
