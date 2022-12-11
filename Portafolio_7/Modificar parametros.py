def buggy(arg, result=[]):
    result.append(arg)
    print(result)


buggy('a', [])
['a']

buggy('b', [])
['b']

buggy('a', ['x', 'y', 'z'])
['x', 'y', 'z', 'a']

buggy('b', ['x', 'y', 'z'])
['x', 'y', 'z', 'b']