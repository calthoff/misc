from error_messages import uppercase_error, z_error, invalid_character_error, number_error, number_of_messages_error
from protocol_1 import ProtocolOne
from tree import Tree


def get_number(string):
    number_ord_list = [i for i in range(48, 58)]
    number = ""
    for c in string:
        if ord(c) in number_ord_list:
            number += c
        else:
            break
    if number:
        return int(number)
    return


class ProtocolTwo(ProtocolOne):
    """
    :param: string with numbers indicating the amount of messages
     followed by lowercase letters a-j and uppercase letters Z M K P Q
    :return: the message and if the message is valid or invalid
    """
    def __init__(self, string):
        super(self.__class__, self).__init__(string)
        self.number = get_number(string)
        self.original_string = self.build_original_string(string)
        self.string_copy = self.original_string
        self.message_count = 0
        self.z_found = False
        self.upper_found = False
        self.m = 0
        self.mz = 0
        self.ml = 0
        self.root_node = Tree(self.string_copy[0])
        first_node = Tree('+')
        self.root_node.insert_child(first_node)
        self.last_node = first_node
        self.first_flag = True

    def check_message(self):
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
            if not self.first_flag:
                new_node = Tree('Z')
                self.last_node.insert_child(new_node)
                self.last_node = new_node
            self.string_copy = self.string_copy[1:]
            flag = self.check_lowercase()
            if flag:
                return self.check_message()
            else:
                return False
        # handle uppercase
        if character in self.upper_case:
            if length < 3:
                uppercase_error()
                return False
            else:
                if not self.first_flag:
                    new_node = Tree(character)
                    self.last_node.insert_child(new_node)
                    self.last_node = new_node
                self.m += 1
                self.upper_found = True
                self.string_copy = self.string_copy[1:]
                return self.check_message()
        # handle lowercase
        if character in self.lower_case:
            is_valid = self.check_lowercase()
            if is_valid:
                if not self.first_flag:
                    new_node = Tree(character)
                    self.last_node.insert_child(character)
                    self.last_node = new_node
                if self.z_found:
                    self.z_found = False
                else:
                    self.message_count += 1
                if self.upper_found:
                    self.ml += 1
                    self.upper_found = False

                self.string_copy = self.string_copy[1:]
                return self.check_message()
            else:
                return False
        invalid_character_error()
        return False

    def build_original_string(self, string):
        if self.number:
            return string[len(str(self.number)):]
        return string

    def count_messages(self):
        self.m -= self.ml + self.mz
        self.message_count += self.mz
        self.message_count += self. m
        self.message_count -= self.ml

    def get_parse_tree(self):
        return self.root_node

    def is_valid(self):
        valid = self.check_message()
        if not self.number:
            number_error()
            return
        self.count_messages()
        if self.message_count != self.number:
            number_of_messages_error()
            return
        if self.message_count == self.number and valid:
            return True
        return

if __name__ == '__main__':
    p = ProtocolTwo('1Za')
    p.check_protocol()