import time


def time_func(f, args, description = 'Description'):
    '''
    Timing wrapper
    '''
    start = time.time()
    result = f(*args)
    elapsed = time.time() - start
    print('Result: {result}'.format(result=result))
    print('{desc}: {sec} seconds'.format(desc=description, sec=elapsed))