#example taken from https://www.codementor.io/python/tutorial/essential-python-interview-questions
class A(object):
    def go(self):
        print("go A go!")
    def stop(self):
        print("stop A stop!")
    def pause(self):
        raise Exception("Not Implemented")

class B(A):
    def go(self):
        super(B, self).go()
        print("go B go!")

class C(A):
    def go(self):
        super(C, self).go()
        print("go C go!")
    def stop(self):
        super(C, self).stop()
        print("stop C stop!")

class D(B,C):
    def go(self):
        super(D, self).go()
        print("go D go!")
    def stop(self):
        super(D, self).stop()
        print("stop D stop!")
    def pause(self):
        print("wait D wait!")

class E(B,C): pass

a = A()
b = B()
c = C()
d = D()
e = E()

# specify output from here onwards

a.go()	#A
b.go()	#A B
c.go()  #A C
d.go()  #A C B D
e.go()  #A C B

a.stop()	#A
b.stop()	#A
c.stop()	#A C
d.stop()	#A C D
e.stop()	#A C

a.pause()
b.pause()
c.pause()
d.pause()
e.pause()
