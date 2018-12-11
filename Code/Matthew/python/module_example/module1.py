
x = 10

def add(a, b):
    return a + b

# print('module 1\'s name: ' + __name__)


print('whatever')


if __name__ == '__main__':
    print('module 1 is being run')
else:
    print('module 1 is being imported into another module that is being run')
