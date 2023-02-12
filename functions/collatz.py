def collatz(number):
    if (number % 2 == 0):
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1

print('Enter an integer:')
try:
    number = collatz(int(input()))
except ValueError:
    print('Integers only.')

while (number != 1):
    number = collatz(number)
