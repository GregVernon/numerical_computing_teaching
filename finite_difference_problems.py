import numpy
def Problem_1():
    f = lambda x: numpy.sin( x )
    df = lambda x: numpy.cos( x )
    N = 10
    x = numpy.linspace( 0, 2*numpy.pi, N )
    dx = # FILL THIS OUT
    exact_deriv = numpy.zeros( N )
    approx_deriv = numpy.zeros( N )
    error = numpy.zeros( N )
    for i in range( 0, N ):
        exact_deriv[i] = df( x[i] )
        if i == 0:
            approx_deriv[i] = # FILL THIS OUT
        elif i == N - 1:
            approx_deriv[i] = # FILL THIS OUT
        else:
            approx_deriv[i] = # FILL THIS OUT
        error[i] = exact_deriv[i] - approx_deriv[i]
    L2_error = numpy.linalg.norm( error, 2 )
    print( exact_deriv )
    print( approx_deriv )
    print( error )
    print( L2_error )

def Problem_2():
    f = lambda x: numpy.sin( x )
    df = lambda x: numpy.cos( x )
    N = 10
    x = numpy.linspace( 0, 2*numpy.pi, N )
    dx = # FILL THIS OUT
    A = numpy.zeros( (N,N) )
    for i in range( 0, N ):
        if i == 0:
            A[0, [_,_,] ] = # FILL THIS OUT
        elif i == N - 1:
            A[N-1, [_,_,] ] = # FILL THIS OUT
        else:
            A[i, [_,_,] ] = # FILL THIS OUT
    approx_deriv = numpy.matmul( A, x )
    exact_deriv = df( x )
    error = exact_deriv - approx_deriv
    L2_error = numpy.linalg.norm( error, 2 )
    print( exact_deriv )
    print( approx_deriv )
    print( error )
    print( L2_error )

def Problem_3():
    f = lambda x: numpy.sin( x )
    d2f = lambda x: -numpy.sin( x )
    ## Fill this out in a similar manner to Problem 1

def Problem_4():
    f = lambda x: numpy.sin( x )
    d2f = lambda x: -numpy.sin( x )
    ## Fill this out in a similar manner to Problem 2