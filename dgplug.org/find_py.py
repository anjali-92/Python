'''        <kushal> Write a function find_py which will take a list as input (use the above mentioned list)
        <kushal> and return the list of python files from it.

'''

def find_py(files):
    return [fil for fil in files if fil.endswith('py')]
    #return [fil for fil in files if fil.find('py') > -1 ] wrong as it will search whole string

def top_files(files):     
    from operator import itemgetter
    top = sorted(files, key = itemgetter(1))[-3:]
    print( top )

if __name__ == '__main__':
    
    files = ['dist', 'MANIFEST.in', 'AUTHORS', '.gitignore', 'setup.py', '.travis.yml', 'README.rst', 'run.py', \
            'gpl.py.txt', '.coveragerc.python', '.git', 'LICENSE', 'appveyor.yml', 'tests', 'Makefile', 'requirements.txt',\
            'conf', 'mu.egg-info', 'mu', 'pyckage', 'CONTRIBUTING.rst', 'docs']

    names = [('dist', 0.4524009038217873), ('MANIFEST.in', 0.7982665626096813),\
            ('AUTHORS', 0.20295547529747415), ('.gitignore', 0.17580804859480004),\
            ('setup.py', 0.43451048336918385), ('.travis.yml', 0.9227925544964634),\
            ('README.rst', 0.15948149348153395), ('run.py', 0.9244602328557816), \
            ('gpl.txt', 0.3660825126160743), ('.coveragerc', 0.9219549563393654), \
            ('.git', 0.7780154704148619), ('LICENSE', 0.26554561400442034), \
            ('appveyor.yml', 0.9138834451991509), ('tests', 0.595527376188135), \
            ('Makefile', 0.16009609575661987), ('requirements.txt', 0.5556594521140621), \
            ('conf', 0.6270727594869117), ('mu.egg-info', 0.5383927558300061),\
            ('mu', 0.23516734243391169), ('package', 0.7701453610852088),\
            ('CONTRIBUTING.rst', 0.18016188734888816), ('docs', 0.5135727736123711)]

    #print(find_py(files))
    top_files( names )
