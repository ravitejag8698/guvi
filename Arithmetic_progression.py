#sum of the n terms in AP
# s = n/2[2a+(n-1)d] where n = no.of terms and d = common difference,a = first term
# formula for nth term is an = a1 + (n-1)d
n,a,d = map(int,input().split())
s = n/2*(2*a+(n-1)*d)
print(int(s))
