'''
Case of mutable default function parameter
'''


def mutbl(test=[2, 3]):
    print(test)
    test.append('5')
    print(test)


def mutblNone(test=None):
    '''
    Will raise exception if deafult is not explicitly
    added like below
    '''
    if not test:
        test = [1, 2]
    print(test)
    test.append('5')
    print(test)


def nonmutbl(test=2222):
    print(test)
    test = 4444
    print(test)


if __name__ == '__main__':
    print('-----Mutable-----')
    print('*** With value ***')
    mutbl(test=[10, 11])
    print('@@@ second call @@@')
    mutbl(test=[10, 11])
    print('*** Without value ***')
    mutbl()
    print('@@@ second call @@@')
    mutbl()

    print('Solution to the issue is setting default value immutable i.e., None')
    print('*** With value ***')
    mutblNone(test=[10, 11])
    print('@@@ second call @@@')
    mutblNone(test=[10, 11])
    print('*** Without value ***')
    mutblNone()
    print('@@@ second call @@@')
    mutblNone()

    print('-----Non-Mutable-----')
    print('*** With value ***')
    nonmutbl()
    print('*** Without value ***')
    nonmutbl()
    print('@@@ second call @@@')
    nonmutbl()
