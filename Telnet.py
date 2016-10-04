import telnetlib,getpass
# user = 'username'
# pw = getpass.getpass()
# host = 'host/ip address'
host = 'localhost'

t = telnetlib.Telnet(host,80)

try:
    # print(t.read_until('login: '))
    # t.write(user + '\n')
    # t.read_until('Password: ')
    # t.write(pw + '\n')

    # t.read_until(' ~ % ' )
    t.write('ls\n')
    print(t.read_until('~ % '))
except Exception as e:
    print(e)
finally:
    t.close()
