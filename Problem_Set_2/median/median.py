def median(a, b, c):
    if a > b:
        if a <= c:
            return a
        elif b <= c:
            return c
        else:
            return b
    elif b <= c:
        return b
    elif a <= c:
        return c
    else:
        return a

if __name__ == '__main__':
    assert median(1,2,3) == 2
    assert median(9,3,6) == 6
    assert median(7,8,7) == 7
    assert median(15,25,90) == 25
    assert median(15,90,25) == 25
    assert median(90,25,15) == 25
    assert median(90,15,25) == 25
    assert median(25,15,90) == 25
    assert median(25,90,15) == 25
