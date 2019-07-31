class Stack:

    def __init__(self):
        self.stack = []
        return

    def push(self,data):
        self.stack.append(data)
        return
    def pop(self):
        if self.stack.__len__()>0:
            return self.stack.pop(self.stack.__len__()-1)
        else:
            return None
    def length(self):
        return self.stack.__len__()