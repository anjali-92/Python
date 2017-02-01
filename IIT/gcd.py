def gcd_1(m, n):
    '''
    This function calculates gcd(gretest common divisor) of numbers 'm' and 'n'
    It creates list of common factors for m and n separately and then two lists 
    are compared to find common factors and then maximum of it is returned
    '''
    print "m value :",m
    print "n value :",n
    fm = []
    for i in range(1,m+1):
        if m%i == 0:
            fm.append(i)

    #print fm

    fn = []
    for i in range(1,n+1):
        if n%i == 0:
            fn.append(i)
    #print fn

    cf = []
    for i in fm:
        if n%i == 0:
            cf.append(i)

    for i in fn:
        if m%i == 0:
            if i not in cf:
                cf.append(i)
    print "gcd_1 gcd is ",cf[-1]

def gcd_2(m, n):
    '''
    In this function, factors are checked from 1 to minimum number(m|n)
    and a list common factor is created and last number is returned
    as gcd.
    '''
    cf = []
    for i in range(1, min(m,n)+1):
        if m%i == 0 and n%i == 0:
            cf.append(i)
    print "gcd_2 gcd is ",cf[-1]

def gcd_3(m, n):
    '''
    In this function we run backward from minimum number to 
    the first greatest common divisor found and this gcd is 
    returned from there.
    '''
    minimum = min(m, n)
    for i in range(minimum, 0,-1):
        if m%i == 0 and n%i == 0:
            print "gcd_3 gcd is ",i
            #return i
            break

def gcd_recursive(m,n):
    '''
    It calculates gcd recursively.
    '''
    if m < n: 
        (m,n) = (n,m)

    if (m % n) == 0:
        return(n)
    else:
        diff = m-n
        return (gcd_recursive(max(n,diff),min(n,diff)))
    
def main():
    '''
    For all the implemented functions time is almost same 
    (same efficiency in computation) it depends on input 
    values m|n depending on that number of checking going
    to happen is decided.
    '''
    gcd_1(6,5)
    gcd_2(6,12)
    gcd_3(6,12)
    gcd_recursive(15,18)
if __name__ == "__main__":
    main()
