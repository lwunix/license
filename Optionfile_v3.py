import os
import re
import shutil

from tempfile import mkstemp
from shutil import move
from os import remove, close

# make a copy of the file first
def copyFile(src, dest):

    try:
        file=shutil.copy(src, dest)
        print(file)
    except shutil.Error as e:
        print('Error: %s' % e)
    except IOError as e:
        print('Error: %s' % e.strerror)


if __name__ == "__main__":

    group = str(input('Enter group name: \n'))
    group = group.upper()
    print(group)

    uid = str(input('Enter the user name: \n'))
    uid = uid.lower()
    print(uid)

    src = '/Users/lwunix/PycharmProjects/work/sample.options'
    dest = '/Users/lwunix/PycharmProjects/work/copy.options'
    copyFile(src, dest)

    pattern = 'GROUP ' + group

with open(dest) as f1:
    with open('output.options', 'a') as f2:
        lines = f1.readlines()
        for i in lines:

            if i.startswith(pattern):
                #index = i.find(' \\')
                # add the uid in the end of the line but before the \ symbol
                #output_line = i[:index] + ' ' + uid + i[index:]
                f2.write(i.replace(pattern, pattern + ' ' + uid))
            else:
                f2.write(i)

