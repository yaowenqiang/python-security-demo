try:
    handle = open('myfile','w')
    handle.write('This is somedata to dump into the file')
    print('Write some data to the file')
except IOError as e:
    print('Exception cought: Unable to write to myfile')
except Exception as e:
    print('Another error occurred!',e)
else:
    print('File written to successfully')
    handle.close()
