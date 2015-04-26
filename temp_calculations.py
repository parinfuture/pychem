'''Counterflow heat exchanger: Calculate X and Y for F, and LMTD calculations'''
import math



def temp_calculations(T1, T2, t1, t2):
    X = (t2-t1)/float((T1 - t1))
    Y = (T1 - T2)/float((t2 -t1))
    LMTD = ((T1-t2) -(T2 - t1))/math.log((T1-t2)/float((T2 - t1)))
#    return X, Y, LMTD
    print "The value of X is: ", X
    print "The value of Y is: ", Y
    print "The value of LMTD is: ", LMTD
          
print temp_calculations(360, 340, 300, 316)
