import __init__

class sample:
    from sample2 import sample2
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = sample2(b)

    def same(self, a):
        self.a = a.get(self.a)
    
    def __str__(self) -> str:
        return f"sample: {self.a}, {self.b}\nsame: {self.same(self.b)}"