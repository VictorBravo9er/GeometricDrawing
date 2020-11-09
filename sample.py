class sample:
    def __init__(self, a, b) -> None:
        from sample2 import sample2
        self.a = a
        self.b = sample2(b)

    def same(self, a):
        self.a = a.get(self.a)
    
    def __str__(self) -> str:
        return f"sample: {self.a}, {self.b}\nsame: {self.same(self.b)}"