# import _winreg
# _winreg works on python 2.7
import winreg

# winreg works on python 2.7
try:
    KeyName = 'myKey'
    key = winreg.CreateKey(winreg.HKEY_CURRENT_USER,"Software\\" + KeyName)
    winreg.SetValueEx(key,'myVal',0,winreg.REG_SZ,'This is a value')
except Exception as e:
    print(e)
