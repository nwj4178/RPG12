class Equipment:
    def __init__(self, name, type_, power):
        self.name = name
        self.type = type_
        self.power = power

    def __str__(self):
        return f"{self.name} (종류: {self.type}, 능력치: {self.power})"
