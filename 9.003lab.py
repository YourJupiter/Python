import os.path

def read_file(fname):
    
    file = open(fname, 'r')
    print('File ' + fname + ':') 
    for line in file:
        print(line, end='') 
    file.close() 
if __name__ == '__main__':

    read_file(os.path.join('data', 'example01.txt'))
