with open('hello.txt', 'rt') as fp:
    for line in fp:
        print(line.rstrip())
        print('=====')


print(f'Файл закрыт? {fp.closed}')

