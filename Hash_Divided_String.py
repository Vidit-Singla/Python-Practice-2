# s= 'abcd'
# k = 2
# l = []
# for i in range(0,len(s),k):
#     l.append(s[i:i+k])

# a=[]
# for i in range(97,123):
#     a.append(chr(i))
# a1= {}
# for ind,nm in enumerate(a):
#     a1[nm] = ind
# print(a1)
# f = ''

# for i in l:
#     ac = 0
#     for j in i:
#         ac += a1[j]
#     s = ac%26
#     f += a1[s]

# print(f)
s = 'abcd'
k = 2
l = []
for i in range(0, len(s), k):
    l.append(s[i:i+k])

a = []
for i in range(97, 123):  
    a.append(chr(i))

a1 = {}
for ind, nm in enumerate(a): 
    a1[nm] = ind

print(a1)

f = '' 

for i in l:
    ac = 0
    for j in i: 
        ac += a1[j]
    s = ac % 26  
    f += a[s] 

print(f)






