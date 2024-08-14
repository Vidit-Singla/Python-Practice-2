def operations(a,b,operator):
    o= {'add':a+b, 'subtract':a-b, 'multiply':a*b, 'divide':a/b}
    return o.get(operator)

result = operations(10,5,'multiply')
print(result)