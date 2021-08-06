from collections import Counter
def fact(n,r):
    prod = 1
    ans = []
    
    for i in range(1,n+1):
        prod *= i
        if i== n-r:
            ans.append(prod)
    ans.append(prod)
    return ans

# code 1
# word =  input('enter a value for word \n')
# print(word)
# n = len(word)
# r = int(input('enter a value for r  (less than length of the word) \n'))
# print(r)
# nrfact,nfact = fact(n,r)
# print(nrfact,nfact)
# print('answer is', nfact//nrfact )

# code2
# word =  input('enter a value for word \n')
# print(word)
# ct = Counter(word)
# n = len(word)
# nrfact,nfact = fact(n,0)
# denominators = [fact(ct[k],0)[-1] for k in ct] 
# nr = nfact
# dr = 1 
# for i in denominators: dr*=i
# print('answer is',nr/dr)

# code for possibilities
# from itertools import permutations
# word =  input('enter a value for word \n')
# print(word)
# perm = permutations(list(word))
# perm = list(set(perm))

# for possibility in list(perm):
#     print(possibility)
