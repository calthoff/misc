

def wrapper(string):
    def f(string):
        lower_case = [i for i in range(97, 107)]
        character = string[0]
        if ord(character) in lower_case:
            return True
        return False
    flag = True
    lower_case = [i for i in range(97, 107)]
    upper_case = [77, 75, 80, 81]
    if len(string) < 1 and flag:
        return True
    if len(string) < 1:
        return False
    character = string[0]
    if character == 'Z':
        if len(string) == 1:
            return False
        string = string[1:]
        flag = f(string)
        if flag:
            return wrapper(string)
        if not flag:
            return False
    if ord(character) in upper_case:
        if len(string) < 3:
            return False
        else:
            return wrapper(string[1:])
    if ord(character) in lower_case:
        is_valid = f(string)
        if is_valid:
            return wrapper(string[1:])
        else:
            return False
    return False

print wrapper('aaaaZaMbbZ')


