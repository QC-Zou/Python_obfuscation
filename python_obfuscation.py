import glob
import os
import time
import subprocess
#
# files_list = glob.glob('E:\PycharmProjects\pyminifier-master\*\*.py')
# print(files_list)


def get_saved_model_path(saved_model_dir):
    model_path_list = []
    for root, dirs, files in os.walk(saved_model_dir):
        for f in files:
            #model_path_list.append(root + "/" + f)
            if f.endswith(".py"):
              model_path_list.append(root + "\\" + f)
    return model_path_list

path_list = get_saved_model_path("G:\soft\\requests\\requests")


list_len = len(path_list)

for i in range(list_len):
    # file_name = path_list[i].split("\.")[-1]
    # print(file_name)

    file = os.path.split(path_list[i])
    print(file)
    # print(file[0])
    # print(file[1])
    #print(file[1][0:-3])


    cmd = '"' + 'D:\Program Files\Python36\Scripts\pyminifier.exe' + '"' + ' -O ' + path_list[i] + ' > ' + file[0] + '\\'+ file[1][0:-3] +'_b.py'
    # with os.popen(cmd, mode='r') as res:
    #     result = res.read()
    #     print()

    returned_value_in_byte = subprocess.Popen(cmd, shell=True)
    print(returned_value_in_byte)

    time.sleep(1)
    if(i>0):
        os.remove(path_list[i-1])
    # with open(path_list[i], 'w', encoding='utf8') as cf:
    #     cf.write(returned_value_in_byte)
    # print("write objs to:", path_list[i])
