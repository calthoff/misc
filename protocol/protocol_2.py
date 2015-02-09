from error_messages import uppercase_error, z_error, invalid_character_error, number_error, number_of_messages_error
from protocol_1 import ProtocolOne


def get_number(string):
    number_ord_list = [i for i in range(48, 58)]
    number = ""
    for c in string:
        if ord(c) in number_ord_list:
            number += c
        else:
            break
    if number:
        return number
    return


class ProtocolTwo(ProtocolOne):
    """
    :param: string with numbers indicating the amount of messages
     followed by lowercase letters a-j and uppercase letters Z M K P Q
    :return: the message and if the message is valid or invalid
    """
    def __init__(self, string):
        self.number = get_number(string)
        self.original_string = self.build_original_string(string)
        self.string_copy = self.original_string
        self.lower_case = [i for i in range(97, 107)]
        self.upper_case = [75, 77, 80, 81]
        self.message_count = 0
        self.z_found = False
        self.upper_found = False
        self.m = 0
        self.mz = 0
        self.ml = 0

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
            self.z_found = True
            if self.upper_found:
                self.mz += 1
                self.upper_found = False
            self.message_count += 1
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
                self.m += 1
                self.upper_found = True
                self.string_copy = self.string_copy[1:]
                return self.wrapper()
        # handle lowercase
        if ord(character) in self.lower_case:
            is_valid = f()
            if is_valid:
                if self.z_found:
                    self.z_found = False
                else:
                    self.message_count += 1
                if self.upper_found:
                    self.ml += 1
                    self.upper_found = False

                self.string_copy = self.string_copy[1:]
                return self.wrapper()
            else:
                return False
        invalid_character_error()
        return False

    def build_original_string(self, string):
        if self.number:
            return string[len(self.number):]
        return string

    def count_messages(self):
        self.m -= self.ml + self.mz
        self.message_count += self.mz
        self.message_count += self. m
        self.message_count -= self.ml

    def check_protocol(self):
        if not self.number:
            number_error()
            return
        self.count_messages()
        print self.message_count
        if self.message_count != self.number:
            number_of_messages_error()
            return
        super(ProtocolTwo, self).check_protocol()

p = ProtocolTwo('2aaZa')
p.check_protocol()