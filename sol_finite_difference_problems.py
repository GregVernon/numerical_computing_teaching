import numpy
def Problem_1():
    f = lambda x: numpy.sin( x )
    df = lambda x: numpy.cos( x )
    N = 10
    x = numpy.linspace( 0, 2*numpy.pi, N )
    dx = x[1] - x[0]
    exact_deriv = numpy.zeros( N )
    approx_deriv = numpy.zeros( N )
    error = numpy.zeros( N )
    for i in range( 0, N ):
        exact_deriv[i] = df( x[i] )
        if i == 0:
            approx_deriv[i] = ( -1.5*f( x[0] ) + 2*f( x[1] ) - 0.5*f( x[2] ) ) / dx
        elif i == N - 1:
            approx_deriv[i] = ( 0.5*f( x[-3] ) - 2*f( x[-2] ) + 1.5*f( x[-1] ) ) / dx
        else:
            approx_deriv[i] = ( 0.5*f( x[i+1] ) - 0.5*f( x[i-1] ) ) / dx
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
    dx = x[1] - x[0]
    A = numpy.zeros( (N,N) )
    for i in range( 0, N ):
        if i == 0:
            A[0, [0, 1, 2] ] = numpy.array( [-3/2, 2, -1/2] ) / dx
        elif i == N - 1:
            A[N-1, [-3, -2,-1] ] = numpy.array( [1/2, -2, 3/2] ) / dx
        else:
            A[i, [i-1, i+1] ] =  numpy.array( [-1/2, 1/2] ) / dx
    approx_deriv = numpy.matmul( A, f( x ) )
    exact_deriv = df( x )
    error = exact_deriv - approx_deriv
    L2_error = numpy.linalg.norm( error, 2 )
    print( exact_deriv )
    print( approx_deriv )
    print( error )
    print( L2_error )
