# import _winreg
# _winreg works on python 2.7
import winreg

# winreg works on python 2.7
KeyName = 'myKey'
try:
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER,"Software\\" + KeyName,0,winreg.KEY_READ) as key:
        if key:
            data = winreg.QueryValueEx(key,'myval')
            print(data)
except Exception as e:
    print(e)
