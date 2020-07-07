import os.path
import datetime
text = '''This text was added in example 2!
Updated
'''
if __name__ == '__main__':
    log_file = os.path.join('data', 'example01.txt')
    with open(log_file, 'a') as log:
        print('\n', text, str(datetime.datetime.now()), file=log)
