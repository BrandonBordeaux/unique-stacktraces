class Stack:
    stack_hash: str = ""
    stack: str = ""
    count: int = 1

    def __init__(self, stack_hash: str, stack: str) -> None:
        self.stack_hash = stack_hash
        self.stack = stack
        self.increment_count()

    def increment_count(self) -> None:
        self.count += 1

    def get_stack_hash(self) -> str:
        return self.stack_hash

    def get_stack(self) -> str:
        return self.stack

    def get_count(self) -> int:
        return self.count
