class OddCounter:
    
    def __init__(self,n=1):
        self.n=n
    def __iter__(self):
        return self
    def __next__(self):
        if self.n<20:
            t=self.n
            self.n+=2
            return t
        raise StopIteration
my_counter=OddCounter()
for x in my_counter:
    print(x,end=' ') 