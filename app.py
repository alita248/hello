print('Hello world!')

file = 'test.tst'

with open(file, mode='w') as f:
    f.write('hello there \n')
    f.write('done \n')

if __name__ == '__main__':
    print('Done') 