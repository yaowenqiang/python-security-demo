import ftblib
f = ftblib.FTP('server ip')

try:
    f.login('username','password')
    print(f.getwelcome())
    f.delete('myfile')
    print(f.dir())
    f.setpasv(1)
    f.storbinary('STOR myfile',open('myfile','rb'))
    print(f.dir())
except Exception as e:
    print('Exception:',e)
finally:
    f.close()
