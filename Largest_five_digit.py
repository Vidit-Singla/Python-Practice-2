# def sumf(n,i):
#     return int(str(n[i])+str(n[i+1])+str(n[i+2])+str(n[i+3])+str(n[i+4]))
# def bigf(n):
#     smax = 0
#     for i in range(len(str(n))):
#         while str(n)[i]!=len(str(n))-4:
#             if sumf(n,i)>smax:
#                 smax = sumf(n,i)
#     print(smax)
# bigf(1234567890)

def findf(n):
    # d={}
    # x = enumerate(str(n))
    # for i,c in x:
    #     d[i]=c
    # v = 

    l = []
    l1 =[]
    n1 = str(n)
    for i in n1:
        x = (n1[int(i):int(i)+5])
        l.append(x)
    l.remove('')

    for j in l:
        l1.append(int(j))
    print(max(l1))
        
    
    
    

findf(123456789)



















