

def swapper(tup):
    x, y = tup
    return (y, x)

def run_swapper(list_of_tuples):
    return list(map(swapper, list_of_tuples))
