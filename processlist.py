import psutil
from pprint import pprint as pp
# l = psutil.get_process_list()
for x in psutil.process_iter():
    if x.name() == 'python':
        # print(x.get_memory_maps())
        pp(x.memory_maps())
