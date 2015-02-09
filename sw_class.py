
def uppercase_error():
    print 'The letters M K P and Q need two valid messages in front of them'

def z_error():
    print 'The letter Z needs one valid message in front of it'

def invalid_character_error():
    print 'messages must only contain lower-case characters a-j and uppercase characters Z M K P and Q'

class Protocol():
    """
    :param: string with lowercase letters a-j and uppercase letters Z M K P Q
    :return: the message and if the message is valid or invalid
    """
    def __init__(self, string):
        self.original_string = string
        self.string = string
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
            character = self.string[0]
            if ord(character) in self.lower_case:
                return True
            return False
        flag = True
        length = len(self.string)
        if length < 1:
            if flag:
                return True
            else:
                return False
        character = self.string[0]
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
            self.string = self.string[1:]
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
                self.string = self.string[1:]
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

                self.string = self.string[1:]
                return self.wrapper()
            else:
                return False
        invalid_character_error()
        return False

    def count_protocol(self):
        print self.message_count
        for i in self.upper_list:
            i = i[0]
            if i == 1:
                self.message_count += 1
            if i >= 3:
                n = i - 2
                self.message_count -= n
        print self.message_count


    def print_result(self, valid):
        if valid:
            print self.original_string , 'VALID'
        else:
            print self.original_string , 'INVALID'

    def check_protocol_1(self, p=True):
        valid = self.wrapper()
        if valid:
            if p:
                self.print_result(valid)
            return True
        if p:
            self.print_result(valid)
        return False

    def check_protocol_2(self):
        valid = self.check_protocol_1(p=False)
        print self.message

p = Protocol('MZaaaMMMMZa')
p.check_protocol_1()
p.count_protocol()
#p.check_protocol_2()
#my suggestion to make this problem more interesting would be to add a step 5 where the parse tree is added to a graph database
# and then displayed on a website