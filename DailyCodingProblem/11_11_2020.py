'''
This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) 
returns the first and last element of that pair. For example, 
car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
'''

'''
This is an example of closure.
A closure is a function object that remembers values
in enclosing scopes even if they are not present in
memory.
'''

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def print_first(a, b):
    print(a)

def car(f):
    f(print_first)

def print_last(a, b):
    print(b)

def cdr(f):
    f(print_last)

if __name__ == '__main__':
    car(cons(3,4))
    cdr(cons(3,4))