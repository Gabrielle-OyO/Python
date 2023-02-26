

def gcd(x,y):
    (x, y) = (y, x) if x>y else (x,y)
    factor=0
    for factor in range(x,0,-1):
        if x % factor == 0 and y % factor == 0:
            return factor


def lcm(x,y):
    gy = x * y // gcd(x,y)
    return gy


