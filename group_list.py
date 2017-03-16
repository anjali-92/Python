#It finds anjali user belongs to which groups


def read_group():
    with open("/etc/group") as fobj:
        for line in fobj:
            #data.append(line.strip())
            line = line.strip().split(':')
            if "anjali" in line and line != []:
                print(line[0])

def read_group1():
    lines = []
    with open("/etc/group") as fobj:
         for line in fobj:
             lines.append(line)

    for line in lines:
        words = line.split(":")
        if words[-1].find("anjali") != -1:
            print(words[0])


read_group()
print("-----")
read_group1()
