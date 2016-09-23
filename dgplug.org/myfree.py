'''
Read /proc/meminfo file and convert first three memory in kb to mb
'''

def calculate_free_memory():
    with file("/proc/meminfo",'r') as file_contents:
        for count in range(0,3,1):
            tokens = file_contents.readline().split(':')
            print tokens[0] + "  "  + str(int(tokens[1].strip().rstrip(' kB'))/1000) + " mB"

if __name__ == '__main__':
    calculate_free_memory()
