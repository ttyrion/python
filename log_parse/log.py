import os
import codecs
from download import download_cupid_files

def GetFilesOfDir(directory):
    filelist = []
    #这个嵌套的for可以列出一个文件夹下的所有文件的全路径，包括子文件夹下的文件
    for parent ,dirs ,files in os.walk(directory):
        for file in files:
            filelist.append(parent+"\\"+file)
    return filelist

current_script_dir = os.sys.path[0]
tmp_dir = current_script_dir + "\\tmp"
print("TMP:" + tmp_dir)

#find out and classify all the log files matching some condition
file_list = GetFilesOfDir(tmp_dir)
for f in file_list:
    print("LOG FILE: " + f)
    full_path = f
    if not os.path.exists(full_path):
        print("不存在："+ full_path)
    file = codecs.open(full_path, encoding="utf-8")
    find = False
    while(True):
        line = file.readline()
        if line == "":
            file.close()
            break
        if line.startswith("Running on machine"):
            file.close()
            find = True
            machine = line.replace("Running on machine: ", "")
            machine = machine.strip("\r\n")
            print("Running on machine: " + machine)
            machine_dir = tmp_dir + "\\" + machine
            if not os.path.exists(machine_dir):
                os.mkdir(machine_dir)
            names = f.split("\\")
            name = names[-1]
            os.system("copy /y %s %s" % (f, machine_dir + "\\" +name) )
            break