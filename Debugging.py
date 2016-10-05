from winappdbg import *
with Debug(bKillOnExit = True) as dbg:
    dbg.execl('calc.exe')

    while dbg:
        try:
            dbg.wait(1000)
        except Exception as e:
            print(e)

        try:
            dbg.dispatch()
        finally:
            dbg.cont()

cmdDbg = Debug()
cmdDbg.system.scan_processes()

# let's look for cmd.exe processes
for ( proc,name  ) in cmdDbg.system.find_processes_by_file_name('cmd.exe'):
    # print out the process ID and the name of the process
    print proc.get_pid(),name
