def plus_two(x):
    return x + 2
 
result1 = list(map(plus_two, [1, 2, 3, 4, 5]))    ##########함수 사용
print(result1) 
 
result2 = list(map((lambda x: x + 2), [1, 2, 3, 4, 5]))   #############람다이용해서 같은 결과값 출력
print(result2)