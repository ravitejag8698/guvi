
n = int(input())
l = map(int,input().split())
ls = list(l)
dic = {}
for i in ls:
    
    
    if i in dic:
        dic[i] += 1
    else:
        
        dic[i] = 1
for k,v in dic.items():
    
    if v == 1:
        
        print(k,end=' ')
   
