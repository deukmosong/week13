def is_even(x):
    return x % 2 == 0
 
 
result1 = list(filter(is_even, range(10)))  ####### 함수 이용
print(result1)
 
result2 = list(filter((lambda x: x % 2 == 0), range(10)))  #####  람다함수이용
print(result2)