def add_commas(number):
    number_string = str(number)
    first_index = len(number_string) % 3
    if first_index == 0:
        first_index = 3
    number_commas = number_string[:first_index]
    number_string = number_string[first_index:]
    while True:
        if not number_string:
            break
        number_commas += ',' + number_string[:3]
        number_string = number_string[3:]
    return number_commas

