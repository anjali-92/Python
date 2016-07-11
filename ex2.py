from collection import OrderedDict
f = file('ex2.txt','r');
dict1 = {}

for line in f.readlines():
	tokens = line.split(':',3)
	dict1[tokens[0]] = int(tokens[2])
	
print OrderedDict(sorted(dict1.items(),key=lambda x: t[0]))

