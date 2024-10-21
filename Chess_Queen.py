t=int(input())
for i in range(t):
    N,X,Y=map(int,input().split())
    moves=(N*2-2)+min(X-1,N-Y)+min(X-1,Y-1)+min(N-X,Y-1)+min(N-X,N-Y)
    print(moves)