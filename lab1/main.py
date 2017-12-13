def fib(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


if __name__ == '__main__':
    while (1):
        inp = input('Введите номер числа фибонначи :')
        if not inp.isnumeric():
            print("ERROR ! введите  подходящее число !")
            continue
        try:
            n = int(inp)
            print("Искомое число : {}".format(fib(n)))
            break
        except Exception:
            print("ERROR ! что-то пошло не так, попробуйте снова")
