import os.path 
text = '''Hello!
I am a text file. And I had been written with a Python
script
before you opened me, so look up the docs and try to delete
me using Python, too.'''

def write_text_to_file(filename, text):

    f = open(filename, "w") 
    f.write(text) 
    f.close()
    
if __name__ == '__main__':
    write_text_to_file(os.path.join('data','example01.txt'), text)
