from functools import reduce
n=reduce((lambda x,y : x+y),range(1,101))
print('에서 100까지의 합:',n)


#######333 2번문제

n=reduce((lambda a,b:a*b),range(1,11))
print("10!=",n)