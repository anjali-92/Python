def gcd_1(m, n):
    '''
    This function calculates gcd(gretest common divisor) of numbers 'm' and 'n'
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
    cf = []
    for i in range(1, min(m,n)+1):
        if m%i == 0 and n%i == 0:
            cf.append(i)
    print "gcd_2 gcd is ",cf[-1]

def gcd_3(m, n):
    cf = []
    minimum = min(m, n)
    for i in range(minimum, 0,-1):
        if m%i == 0 and n%i == 0:
            print "gcd_3 gcd is ",i
            break

def main():
    gcd_1(6,5)
    gcd_2(6,12)
    gcd_3(6,12)

if __name__ == "__main__":
    main()
