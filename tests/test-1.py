

def fun(i):
    for a in range(i):
        if a % 2 == 0:
            raise Exception
        yield (i)

def fun2(i):
    a = fun(i)
    for b in range(i):
        try:
            print(a.__next__())
        except:
            continue

fun2(10)