class Stack:
    stack_hash = ""
    stack = ""
    count = 1

    def __init__(self, stack_hash, stack):
        self.stack_hash = stack_hash
        self.stack = stack
        self.increment_count()

    def increment_count(self):
        self.count += 1

    def get_stack_hash(self):
        return self.stack_hash

    def get_stack(self):
        return self.stack

    def get_count(self):
        return self.count
