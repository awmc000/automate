def div42(by):
    try:
        return 42 / by
    except ZeroDivisionError:
        print('Error: bad argument.')

print(div42(0))
print(div42(1))
print(div42(42))
