def test(*args):
    print('test')
    print(args)
    for i, arg in enumerate(args):
        print("параметры:", i, arg)


test(28, 1, 1977, 'Sergei')

def faktorial(n):
    if n == 1:
        return 1
        faktorial_n_minus_1 * faktorial(n=n -1)

        return n * faktorial_n_minus_1

print(faktorial(2))

