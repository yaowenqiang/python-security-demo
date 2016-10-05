import os
import datetime

rootdir='/home/jack/pyproject/security/'
searchdate = datetime.date.today() - datetime.timedelta(days=1)
print(searchdate)

for curr,dirs,files in os.walk(rootdir):
    for f in files:
        try:
            path = "{}/{}".format(curr,f)
            t = datetime.date.fromtimestamp(os.path.getmtime(path))
            if t < searchdate:
                print('found date {} - {}'.format(path,t))
        except Exception as e:
            print(e)
            no_op = 0
