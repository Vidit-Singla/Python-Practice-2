def accum(s):
    result = []
    for i in range(len(s)):
        result.append((s[i] * (i + 1)).capitalize())
    return '-'.join(result)

print(accum('abcd'))