'''
http://stackoverflow.com/questions/3501382/checking-whether-a-variable-is-an-integer-or-not/3501408#3501408
'''

#def find_numbers(find):
#    return [i for i in find if type(i) == int ]

#def find_numbers(find):
#    return [i for i in find if isinstance(i , int) ]
    

if __name__ == '__main__':
   print( find_numbers([ 1, 'abc', 'xyz', 2.15, 6.7 ]) )
