####1번문제
n_list=[1,2,3,4,5,6,7,8,9,10]
even_list=[]
for a in filter(lambda x : x%2==0,n_list):
    even_list.append(a)
print(even_list)
####1-2번문제
even_list=[]
even_list=list(filter(lambda x :x%2==0,n_list))
print(even_list)

#############2-1번문제
odd_list=[]
for a in filter(lambda x : x%2==1 ,n_list):
    odd_list.append(a)
print(odd_list)

###########2-2번문제
odd_list=[]
odd_list=list(filter(lambda x :x%2==1,n_list))
print(odd_list)