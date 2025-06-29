

def recursive_fastex(b :int, e :int) -> int :

    if not e : return 1
    r = recursive_fastex(b,e >>1)
    return (b*r*r if e &1 else r*r)


def iterative_fastex(b :int, e :int) -> int :

    r = 1

    while   0 <e:
        if  e &1 : r = (r*b)

        b = (b*b)
        e >>= 1

    return r

