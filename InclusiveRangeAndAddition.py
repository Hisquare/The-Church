# A PROGRAM THAT ALLOWS A USER INPUT A VALUE INTO A RANGE FUNCTION FOR AN INCLUSIVE RANGE. ALSO TO PRINT ITS SUM.
def u_range(*args):
    biker = len(args) # numargs equal length of argument
    if biker < 1: raise TypeError ("you must enter at least one argument")
    elif biker == 1:
        stop = args[0] # [0] is doing nothing here. its optional.
        start = 0
        step = 1
    elif biker == 2:
        step = 1
        (start, stop) = args
    elif biker == 3:
        (start, stop, step) = args
    else: raise TypeError('three arguments required. but you entered {}'.format(biker))
# 'else' works when numargs is not 1,2,3.
    i = start
    while i <= stop:
        yield i
        i += step

start = int(input('enter start: '))
stop = int(input('enter stop: '))
step = int(input('enter step: '))

number = u_range(start,stop,step)

# to sum the individual values of the range 
def bingo(): # be sure to indent properly
    summ = 0
    for i in number:
        summ += i
    return summ

# to print
print(bingo(), end = ' ')
