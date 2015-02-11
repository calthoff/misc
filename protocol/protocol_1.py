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
    def count_nodes(self, count=-1):
        lower_case = [chr(i) for i in range(97, 107)]
        flag = True
        for c in self.data:
            if c not in lower_case:
                flag = False
        if flag:       
            count += len(self.data)
        else:
            count += 1
        if self.left_child:
            return self.left_child.count_nodes(count)
        return count
        
   
class Protocol(object):
    """
    :param: string with lowercase letters a-j and uppercase letters Z M K P Q
    :return: the message and if the message is valid or invalid
    """
    def __init__(self, string):
        self.string = string
        self.lower_case = [chr(i) for i in range(97, 107)]
        self.upper_case = ['M', 'K', 'P', 'Q']
        self.valid_characters = self.lower_case + self.upper_case + ['Z']

        self.double_m = 0
        self.single_m = 0

    def check_message(self, string):
        length = len(string)
        character = string[0]
        # handle rule 1
        if character not in self.valid_characters:
            print 'invalid character'
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
        # ZaZa
        if character in self.lower_case:
            return self.check_message(string[1:])
        # handle rule 3
        if character == 'Z':
            left_child = self.check_message(string[1:])
            if left_child:
                node = TreeNode(string)
                node.prefix = 'Z'
                node.left_child = left_child
                return node
        # handle rule 4
        if character in self.upper_case:
            # MMaZa
            if len(string) > 2:
                if string[1] in self.upper_case:
                    self.double_m += 1
                    return self.check_message(string[1:])
                #count
                if string[1] == 'Z':
                    self.double_m +=1
            ros = string[1:]
            for i in range(1, len(ros)):
                x = ros[0:i]
                y = ros[i:]
                print x, ',', y
                if not x or not y:
                    return None
                left_child = self.check_message(x)
                right_child = self.check_message(y)
                if left_child and right_child:
                    node = TreeNode(string)
                    node.prefix = character
                    node.left_child = left_child
                    node.right_child = right_child
                    return node
        return None
    
    def print_result(self, valid):
        if valid:
            print self.string, 'VALID'
            print valid.print_tree()
            print valid.count_nodes()
        else:
            print self.string, 'INVALID'

    def check_protocol(self):
        valid = self.check_message(self.string)
        self.print_result(valid)

if __name__ == '__main__':
    p = Protocol('MMMMMMaZa')
    p.check_protocol()