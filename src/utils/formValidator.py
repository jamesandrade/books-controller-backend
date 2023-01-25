class FormValidator():
    def isValid(*args, data=[]):
        for i in args:
            if i in data:
                if data[i] == None:
                    return False
            else:
                return False
        return True