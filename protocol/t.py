from error_messages import uppercase_error, z_error, invalid_character_error


class ProtocolOne(object):
    """
    :param: string with lowercase letters a-j and uppercase letters Z M K P Q
    :return: the message and if the message is valid or invalid
    """
    def __init__(self, string):
        self.original_string = string
        self.string_copy = string
        self.lower_case = [chr(i) for i in range(97, 107)]
        self.upper_case = ['M', 'K', 'P', 'Q']

    def check_lowercase(self):
        c = self.string_copy[0]
        if c in self.lower_case:
            return True
        return False

    def check_message(self):
        length = len(self.string_copy)
        if length < 1:
            return True
        character = self.string_copy[0]
        # handle z
        if character == 'Z':
            if length == 1:
                z_error()
                return False
            self.string_copy = self.string_copy[1:]
            z_test = self.check_lowercase()
            if z_test:
                return self.check_message()
            return False
        # handle uppercase
        if character in self.upper_case:
            if length < 3:
                uppercase_error()
                return False
            self.string_copy = self.string_copy[1:]
            return self.check_message()
        # handle lowercase
        if character in self.lower_case:
            lower_test = self.check_lowercase()
            if lower_test:
                self.string_copy = self.string_copy[1:]
                return self.check_message()
            return False
        invalid_character_error()
        return False

    def print_result(self, valid):
        if valid:
            print self.original_string, 'VALID'
        else:
            print self.original_string, 'INVALID'

    def is_valid(self):
        return self.check_message()

    def check_protocol(self):
        valid = self.is_valid()
        self.print_result(valid)

if __name__ == '__main__':
    p = ProtocolOne('MZa')
    p.check_protocol()
