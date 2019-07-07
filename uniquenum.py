
n = int(input())
l = map(int,input().split())
ls = list(l)
dict = {}
for i in ls:
    
    
    if i in dict:
        dict[i] += 1
    else:
        
        dict[i] = 1
for k,v in dict.items():
    
    if v == 1:
        
        print(k,end=' ')
   
