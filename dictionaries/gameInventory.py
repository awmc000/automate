import pprint


def displayInventory(invDict):
    print('Inventory:')
    
    totalItems = 0 # accumulator
    
    for k, v in invDict.items():
        print(str(v) + ' ' + k)
        totalItems += v

    print(f'Total number of items: {totalItems}')

def listToDictionary(l):
    newDict = {}
    for elem in l:
        newDict.setdefault(elem, 0)
        newDict[elem] += 1
    return newDict

testInv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

displayInventory(testInv)
pprint.pprint(listToDictionary(['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']))