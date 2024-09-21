t = int(input())
f = []
for __ in range(t):
    n = int(input())
    y = input()
    if 'I' in y:
        f.append('INDIAN')
    elif 'I' not in y:
        if 'N' in y and 'Y' in y:
            f.append("NOT INDIAN")
        
        else:
            f.append("NOT SURE")

for i in f:
    print(i)

    