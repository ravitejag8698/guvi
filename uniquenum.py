
n = int(input())
l = map(int,input().split())
ls = list(l)
dict = {}
for i in ls:
    
    
    if i in dict:
        dict[i] += 1
    else:
        
        dict[i] = 1
for key,val in dict.items():
    
    if val == 1:
        
        print(key,end=' ')
   
