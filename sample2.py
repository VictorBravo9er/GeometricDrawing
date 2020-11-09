class sample2:
    def __init__(self,b) -> None:
        self.b = b
    
    def get(self, a):
        from sample import sample
        a = sample(a,self.b)
        return(self.b - a.a)

    def __str__(self) -> str:
        return f"sample2: {self.b}\nget: {self.get(2)}"
