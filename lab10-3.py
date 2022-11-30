##############1-1번문제
lista=['a','b','c','d']
upper_a_list=[]
def to_upper(a):
    return a.upper()
for i in lista:
    upper_a_list.append(to_upper(i))

print(upper_a_list)
######1-2번문제
upper_a_list=[]
upper_a_list=list(map(lambda a:a.upper(),lista))
print(upper_a_list) 
#########2-1번문제
n_list=[10,20,30]
def twice(a):
    return 2*a
def triple(a):
    return 3*a
double_n=list(map(twice,n_list))
triple_n=list(map(triple,n_list))
print('입력값의 두 배:',double_n)
print('입력값의 세 배:',triple_n)
#############2-2번문제
double_n=list(map(lambda x : 2*x,n_list))
triple_n=list(map(lambda x : 3*x,n_list))
print('입력값의 두 배:',double_n)
print('입력값의 세 배:',triple_n)




