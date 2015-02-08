

def print_uppercase_error():
    print 'The letters M K P and Q need two valid messages in front of them'

def print_z_error():
    print 'The letter Z needs one valid message in front of it'

class Protocol():
    """
    :param: string
    :return: message and if the message is valid
    """
    def __init__(self, string):
        self.original_string = string
        self.string = string
        self.character = self.string[0]
        self.lower_case = [i for i in range(97, 107)]
        self.upper_case = [75, 77, 80, 81]

    def wrapper(self):
        def f():
            if ord(self.character) in self.lower_case:
                return True
            return False
        flag = True
        length = len(self.string)
        if length < 1:
            if flag:
                return True
            else:
                return False
        if self.character == 'Z':
            if length == 1:
                print_z_error()
                return False
            self.string = self.string[1:]
            flag = f()
            if flag:
                return self.wrapper()
            else:
                return False
        if ord(self.character) in self.upper_case:
            if length < 3:
                print_uppercase_error
                return False
            else:
                self.string = self.string[1:]
                return self.wrapper()
        if ord(self.character) in self.lower_case:
            is_valid = f()
            if is_valid:
                self.string = self.string[1:]
                return self.wrapper()
            else:
                return False
        return False

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
        if valid:
            message_count = 0
            total_count = len(self.original_string)
            for c in self.original_string:
                if total_count <= 0:
                    break
                #print total_count
                if ord(c) in self.lower_case:
                    total_count -= 1
                    message_count += 1
                if ord(c) in self.upper_case:
                    total_count -= 3
                    message_count += 1
                if c == 'Z':
                    total_count -= 2
                    message_count += 1
            print message_count
        self.print_result(valid)
        return False

    def print_result(self, valid):
        if valid:
            print self.original_string , 'VALID'
        else:
            print self.original_string , 'INVALID'


p = Protocol('aaaaZaMbb')
#p.check_protocol_1()
p.check_protocol_2()