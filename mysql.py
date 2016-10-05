import MySQLdb
import pdb

try:
    db = MySQLdb.connect(host='localhost',user='root',passwd='123456',db='myDB')
    # pdb.set_trace()
    curs = db.cursor()
    curs.execute('select * from tblGrades')

    for row in curs.fetchall():
        # print("Name: {} Grade: {}".format(row[1],row[2]))
        print("Name: {} Grade: {}".format(row[1],row[2]))
    # print("Name: {} Grade: {}".format(row[1],row[2]))
except Exception as e:
    print(e)

