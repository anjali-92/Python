######################################################################
# 1. Accept number of elements to be print from user and print following
# pattern
# * * * * * *

for i in range(6):
    print '*',

print '\n------------------------'    
######################################################################
# 2. Accept number of elements to be print from user and print following
# pattern
# 1 1 1 1 1 1

print
for i in range(5):
    print '1',

print '\n------------------------'    
######################################################################
# 3. Accept number of elements to be print from user and print following
# pattern
# 1 2 3 4 5 6

print
for i in range(6):
    print str(i+1),

print '\n------------------------'    
######################################################################
# 4. Accept number of elements to be print from user and print following
# pattern
# 1 3 5 7 9 10

print
for i in range(1,10):
    if i%2 != 0:
        print i,

print '\n------------------------'    
######################################################################
# 5. Accept number of elements to be print from user and print following
# pattern
# a a a a a a

print
for i in range(5):
    print 'a',

print '\n------------------------'    
######################################################################
# 6. Accept number of elements to be print from user and print following
# pattern
# A A A A A A

print
for i in range(5):
    print 'A',

print '\n------------------------'    
######################################################################
# 7. Accept number of elements to be print from user and print following
# pattern
# a b c d e f

print
for i in range(ord('a'), ord('f')):
    print chr(i),

print '\n------------------------'    
######################################################################
# 8. Accept number of elements to be print from user and print following
# pattern
# a c e g i k

print
for i in range(96,107):
    if i%2 != 0:
        print chr(i),

print '\n------------------------'    
######################################################################
# 9. Accept number of elements to be print from user and print following
# pattern
# A B C D E F

print
for i in range(ord('A'), ord('G')):
    print chr(i),

print '\n------------------------'    
######################################################################
# 10. Accept number of rows from user and print following pattern
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

print
for i in range(5):
    for j in range(5):
        print '* ',
    print

print '------------------------'    
######################################################################
# 
# 11.Accept number of rows from user and print following pattern
# a a a a
# a a a a
# a a a a
# a a a a

print
for i in range(5):
    for j in range(5):
        print 'a ',
    print

print '------------------------'    
######################################################################
# 12.Accept number of rows from user and print following pattern
# a b c d
# a b c d
# a b c d
# a b c d

print
for i in range(5):
    for j in range(ord('a'), ord('e')):
        print chr(j),
    print

print '------------------------'    

######################################################################
# 13.Accept number of rows from user and print following pattern
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4

print
for i in range(4):
    for j in range(4):
        print j+1 ,
    print

print '------------------------'    


######################################################################
# 14.Accept number of rows from user and print following pattern
# 1 2 3 4
# 5 0 0 6
# 7 0 0 8
# 9 10 11 12

print
cnt=1
for i in range(4):
    for j in range(4):
        if i == 0 or i == 3 or j == 0 or j == 3:
            print cnt,
            cnt = cnt + 1
        else:
            print '0',
    print

print '------------------------'    

######################################################################
# 15.Accept number of rows from user and print following pattern
# *
# * *
# * * *
# * * * *
# * * * * *

print
for i in range(5):
    for j in range(5):
        if j <= i:
            print '* ',
    print

print '------------------------'    

######################################################################
# 16.Accept number of rows from user and print following pattern
# *
# * *
# * - *
# * - - *
# * - - - *

print
for i in range(5):
    for j in range(5):
        if j == i or j == 0:
            print '*',
        elif j>i :
            print ' ',
        else:
            print '-',
    print

print '------------------------'    

######################################################################
# 17.Accept number of rows from user and print following pattern. (- is blank
# space)
# * * * * *
# * - - - *
# * - - - *
# * - - - *
# * * * * *

print
for i in range(5):
    for j in range(5):
        if j == 4 or j == 0 or i == 0 or i == 4:
            print '*',
        else:
            print '-',
    print

print '------------------------'    

######################################################################
# 18.Accept number of rows from user and print following pattern. (- is blank
# space)
# * * * * *
# * * - - *
# * - * - *
# * - - * *
# * * * * *

print
for i in range(5):
    for j in range(5):
        if j == 4 or j == 0 or i == 0 or i == 4 \
           or i == j:
            print '*',
        else:
            print '-',
    print

print '------------------------'    

######################################################################
# 19.Accept number of rows from user and print following pattern. (- is blank
# space)
# * * * * *
# * * * *
# * * *
# * *
# *

print
jn = 5
for i in range(5):
    for j in range(jn):
        print '*',
    jn = jn -1
    print

print '------------------------'    

######################################################################
# 
# 20.Accept number of rows from user and print following pattern.
# * * * * *
# * * * *
# * * *
# * *
# *

print
jn = 5
for i in range(5):
    for j in range(jn):
        print '*',
    jn = jn -1
    print

print '------------------------'    

######################################################################
# 21.Accept number of rows from user and print following pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

print
for i in range(6):
    for j in range(6):
        if j < i:
            print j+1,
    print

print '------------------------'    
#####################################################################
# 22.Accept number of rows from user and print following pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

print
rows = 8
for i in range(rows):
    for j in range(rows):
        if j < i:
            print j+1,
    print
jn = rows - 2
for i in range(rows-2):
    for j in range(jn):
        print j+1,
    print
    jn = jn - 1
 
print '------------------------'    
######################################################################
# 23.Accept number of rows from user and print following pattern
# 1
# 0 0
# 1 2 3
# 0 0 0 0
# 1 2 3 4 5

print
for i in range(6):
    for j in range(i):
        if i%2 == 0:
            print '0',
        else:
            print j+1,
    print
print '------------------------'    

######################################################################
# 24.Accept number of rows from user and print following pattern
# 1
# 1 0
# 1 0 3
# 1 0 3 0
# 1 0 3 0 5

print
for i in range(6):
    for j in range(i):
        if (j+1)%2 == 0:
            print '0',
        else:
            print j+1,
    print
print '------------------------'    

######################################################################
# 
# 25.Accept number of rows from user and print following pattern
# 1
# 1 2
# 1 0 3
# 1 0 0 4
# 1 0 0 0 5

print
for i in range(5):
    for j in range(i):
        if j == 0 or j == i-1:
            print j+1,
        elif j< i:
            print 0,
        else:
            print ' ',
    print

print '------------------------'    
######################################################################
# 26.Accept number of rows from user and print following pattern
# 1
# 1 1
# 1 0 1
# 1 0 0 1
# 1 0 0 0 1

print
for i in range(6):
    for j in range(i):
        if j == 0 or j == i-1:
            print 1,
        elif j< i:
            print 0,
        else:
            print ' ',
    print

print '------------------------'    
######################################################################
# 27.Accept number of rows from user and print following pattern
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

print
for i in range(6):
    for j in range(i):
        if j <= i:
            print i,
    print

print '------------------------'    

######################################################################
# 28.Accept number of rows from user and print following pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


print
for i in range(6):
    for j in range(i):
        if j <= i:
            print j+1,
    print

print '------------------------'    

######################################################################
# 29.Accept number of rows from user and print following pattern
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

print
cnt=1
for i in range(6):
    for j in range(i):
        if j <= i:
            print cnt,
            cnt = cnt + 1
    print

print '------------------------'    

######################################################################
# 30.Accept number of rows from user and print following pattern
# 1
# 4 9
# 16 25 36

print
cnt=1
for i in range(5):
    for j in range(i+1):
        if j <= i:
            print cnt * cnt,
            cnt = cnt + 1
    print

print '------------------------'    

######################################################################
# 31.Accept number of rows from user and print following pattern
# 1
# 4 9
# 7 7 9
# 13 10 9 1



######################################################################
# 32.Accept number of rows from user and print following pattern
# 10
# 20 21
# 30 31 32
# 40 41 42 43
# 50 51 52 53 54

print
cnt=10
for i in range(5):
    for j in range(i+1):
        if j <= i:
            print cnt+j,
    print
    cnt = cnt + 10

print '------------------------'    

######################################################################
# 33.Accept number of rows from user and print following pattern
# 1
# 2 3
# 4 5 6
# 7 8 9 1
# 2 3 4 5 6

print
cnt=1
for i in range(5):
    for j in range(i+1):
        if j <= i:
            print cnt,
            cnt = cnt + 1
        if cnt == 10:
            cnt = 1
    print

print '------------------------'    

######################################################################
# 34.Accept number of rows from user and print following pattern
# 1
# 1 1
# 1 0 1
# 1 0 0 1
# 1 0 0 0 1
# 1 1 1 1 1 1

print
row = 5
for i in range(row):
    for j in range(i):
        if j == 0 or j == i-1 or i == row-1:
            print 1,
        elif j< i:
            print 0,
        else:
            print ' ',
    print

print '------------------------'    

######################################################################
# 35.Accept number of rows from user and print following pattern
#          1
#        1 1 1
#      1 0 1 0 1
#    1 0 0 1 0 0 1
#  1 0 0 0 1 0 0 0 1
#1 1 1 1 1 1 1 1 1 1 1
#

print
rows = 6
for i in range(rows):
    for j in range(rows*2-1):
        if i == rows-1 or j == rows-1:
            print 1,
        elif j == (rows-1)-i or j == (rows-1)+i:
            print 1,
        elif (j > (rows-1)-i and j < (rows-1)) or (j < (rows-1)+i and j > (rows-1)) :
            print 0,
        else:
            print ' ', 
    print

print '------------------------'    

######################################################################
# 36.Accept number of rows from user and print following pattern
# 0
# 1 1
# 2 3 5
# 8 13 21 34

print
rows = 4
a1 = 1
a2 = 1
a3 = 0
for i in range(rows):
    for j in range(i+1):
        print a3,
        a1 = a2
        a2 = a3
        a3 = a1 + a2
    print
print '\n------------------------'    

######################################################################
# 37.Accept number of rows from user and print following pattern
# 1
# 1 1
# 1 2 3
# 1 2 3 6
# 1 2 3 4 10

print
val = 0
for i in range(5):
    for j in range(i+1):
        if j == i:
            print val,
        else:
            print j+1,
            val = val + j + 1 
    print
    val = 0
print '\n------------------------'    

######################################################################
# 38.Accept number of rows from user and print following pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 4 6 6 4 0

print
rows = 5
col_sum = [0 for i in range(rows)]
for i in range(rows):
    for j in range( i+1 ):
        if i == rows - 1:
            print col_sum[j],
        else:
            col_sum[j] = col_sum[j] + j + 1
            print j+1,
    print

print '\n------------------------'    
######################################################################
# 39.Accept string from user and print in following format.
# Input string : PIYUSH
# Output :
# A
# A N
# A N J
# A N J A
# A N J A L
# A N J A L I

print
name = ['A', 'N', 'J', 'A', 'L', 'I']
for i in range(len(name)):
    for j in range(i+1):
        print name[j],
    print

print '\n------------------------'    
# 40.Accept string from user and print in following format.
# Input string : PIYUSH
# Output :
# P I Y U S H
# P I Y U S
# P I Y U
# P I Y
# P I
# P
# 
print '\n------------------------'    
######################################################################
# 41.Accept string from user and print in following format.
# Input string : PIYUSH
# P i Y u S h
# P i Y u S
# P i Y u
# P i Y
# P i
# P
print '\n------------------------'    
######################################################################
# 42.Accept string from user and print in following format.
# Input string : UNIX WIN32 SDK
# U
# U N
# U N I
# U N I X
# W
# W I
# W I N
# W I N 3
# W I N 3 2
# S
# S D
# S D K
print '\n------------------------'    
######################################################################
# 43.Accept string from user and print in following format.
# Input string : UNIX WIN32 SDK
# U
# U N
# U N I
# U N I X
#       W
# 	  W I
# 	  W I N
# 	  W I N 3
# 	  W I N 3 2
# 			  S
# 			  S D
# 			  S D K
print '\n------------------------'    
######################################################################
# 43.Accept n from user and print in following format.
#     5
#   5 4
# 5 4 3
#   3 2
#     1

print '\n------------------------'    







