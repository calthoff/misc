from error_messages import uppercase_error, z_error, invalid_character_error


class ProtocolOne(object):
    """
    :param: string with lowercase letters a-j and uppercase letters Z M K P Q
    :return: the message and if the message is valid or invalid
    """
    def __init__(self, string):
        self.original_string = string
        self.string_copy = string
        self.lower_case = [i for i in range(97, 107)]
        self.upper_case = [75, 77, 80, 81]

    def wrapper(self):
        def f():
            c = self.string_copy[0]
            if ord(c) in self.lower_case:
                return True
            return False
        flag = True
        length = len(self.string_copy)
        if length < 1:
            if flag:
                return True
            else:
                return False
        character = self.string_copy[0]
        # handle z
        if character == 'Z':
            if length == 1:
                z_error()
                return False
            self.string_copy = self.string_copy[1:]
            flag = f()
            if flag:
                return self.wrapper()
            else:
                return False
        # handle uppercase
        if ord(character) in self.upper_case:
            if length < 3:
                uppercase_error()
                return False
            else:
                self.string_copy = self.string_copy[1:]
                return self.wrapper()
        # handle lowercase
        if ord(character) in self.lower_case:
            is_valid = f()
            if is_valid:
                self.string_copy = self.string_copy[1:]
                return self.wrapper()
            else:
                return False
        invalid_character_error()
        return False

    def print_result(self, valid):
        if valid:
            print self.original_string, 'VALID'
        else:
            print self.original_string, 'INVALID'

    def check_protocol(self):
        valid = self.wrapper()
        if valid:
            self.print_result(valid)
        else:
            self.print_result(valid)

if __name__ == '__main__':
    p = ProtocolOne('aaZa')
    p.check_protocol()