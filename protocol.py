from error_messages import uppercase_error, z_error, invalid_character_error

class TreeNode:
    def __init__(self, data=""):
        self.data = data
        self.prefix = ""
        self.left_child = None
        self.right_child = None
        
    def print_tree(self, indentation=''):
        print indentation, self.data, self.prefix
        if self.left_child:
            indentation += '   '
            self.left_child.print_tree(indentation)
            if self.right_child:
                self.right_child.print_tree(indentation)
        
   
class ProtocolOne(object):
    """
    :param: string with lowercase letters a-j and uppercase letters Z M K P Q
    :return: the message and if the message is valid or invalid
    """
    
    lower_case = [chr(i) for i in range(97, 107)]
    upper_case = ['M', 'K', 'P', 'Q']
    valid_characters = lower_case + upper_case + ['Z']
           
    def check_message(self, string):
        length = len(string)
        character = string[0]
        # handle rule 1
        if character not in self.valid_characters:
            return None
        # handle rule 2
        if length == 1:
            if character not in self.lower_case:
                return None
            return TreeNode(character)
        lower_flag = True
        for c in string:
            if c not in self.lower_case:
                lower_flag = None
        if lower_flag:
            return TreeNode(string)
        # handle rule 3
        if character == 'Z':
            left_child = self.check_message(string[1:])
            if left_child:
                node = TreeNode(string)
                node.prefix = 'Z'
                node.left_child = left_child
                return node
        # handle rule 4
        if character not in self.upper_case:
            return None
        ros = string[1:]
        for i in range(1, len(ros)):
            x = ros[0:i]
            y = ros[i:]
            left_child = self.check_message(x)
            right_child = self.check_message(y)
            if left_child and right_child:
                node = TreeNode(string)
                node.prefix = character
                node.left_child = left_child
                node.right_child = right_child
                return node
        return None
    
    def print_result(self, string, node):
        if node:
            print string, 'VALID'
            print node.print_tree()
        else:
            print string, 'INVALID'
        
    def is_valid(self, string):
        if len(string) < 1:
            return False
        return self.check_message(string)

    def check_protocol(self, string):
        string_list = string.strip().split()
        for s in string_list:
            node = self.is_valid(s)
            self.print_result(s,node)

    def count_valid(self, string, count=0):
        for i in range(1,len(string)+1):
            left = string[0:i]
            right = string[i:]
            if self.check_message(left):
                return self.count_valid(right,count+1)
        return count      

def main_test(string):
    p = ProtocolOne()
    p.check_protocol(string)

def bonus1_(string):
    number_list = [chr(i) for i in range(48, 58)]
    number = ""
    for c in string:
        if c in number_list:
            number += c
        else:
            break
    p = ProtocolOne()
    string = string[len(number):]
    print string 
    count = p.count_valid(string)
    print number, count 
    if int(number) == count:
        print string, 'valid', count
    else:
        print string, 'invalid', count
        
if __name__ == '__main__':
    main_test('Za Mbb')
    bonus1_('10aaaaaaaaaa')
    #print string, p.count_valid(string)
