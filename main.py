def test_(a = 1, b = 'Snooker', c = True):
    print(a, b, c)

test_()

def fact(n):
    if n == 1:
        return 1
    return fact(n-1)*n

print(fact(6))