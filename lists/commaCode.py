import sys

def commaList(list):
    string = ''
    for i in range(len(list) - 1):
        string += str(list[i]) + ', '
    string += 'and ' + list[-1] + '.'
    return string

print(commaList(sys.argv[1::]))

