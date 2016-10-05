import os
rootdir = '/'

for curr,dirs,files in os.walk(rootdir):
    for f in files:
        path = "{}/{}".format(curr,f)
        print(path)
