class EvenCounter:
    def __init__(self,n=0):
        self.n=n
    def __iter__(self):
        return self
    def __next__(self):
        t=self.n
        self.n+=2
        return t

my_even=EvenCounter()
print(next(my_even),end=' ')
print(next(my_even),end=' ')
print(next(my_even),end=' ')
print(next(my_even),end=' ')
print(next(my_even),end=' ')
print('')
my_even=EvenCounter()

##############2번 문제
for x in my_even :
    if x>20:
        break
    print(x,end=' ')

