import poplib,imaplib,getpass
p = poplib.POP3('serverip',110)
# p = poplib.POP3_SSL('ip',995)

print(p.getwelcome())
p.user('username')
p.pass_('password')
print(p.list())

i = imaplib.IMAP4('ip',143)
# i.login(getpass.getuser(),getpass.getpass_())
i.login('username','password')
i.select()
t,l = i.list()
print('Response code: ',t)
print(l)

t,ids = i.search(None,'ALL')
print("Response code: ",t)
print(ids)
t,msg = i.fetch('1','(UID BODY[TEXT])')
# store messages on the server
# i.store()
print(msg)
i.close()
i.logout()
