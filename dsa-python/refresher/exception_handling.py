try:
    ''' some long_running_function()'''
except KeyboardInterrupt:
    print('Keyboard interrupted long running function')
except IndexError:
    print('Index out of range during long running function')
    raise Exception(" Raised an exception")