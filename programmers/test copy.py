def chain(*iterables):
    
    for it in iterables:
        print(it)
        for i in it:
            yield i

s = 'ABC'
t = tuple(range(3))
print(list(chain(s, t)))
