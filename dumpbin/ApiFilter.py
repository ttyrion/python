import os
import codecs

def GetFilesOfDir(directory):
    filelist = []
    #recursively find the executable files in a directory
    for parent ,dirs ,files in os.walk(directory):
        for file in files:
            if file.endswith("dll") or file.endswith("exe"):
                filelist.append(parent+"\\"+file)
    return filelist

current_script_dir = os.sys.path[0]
print(current_script_dir + ":")
executables = GetFilesOfDir(current_script_dir);

results_dir = current_script_dir + "\\results\\"
if os.path.exists(results_dir):
    os.system("rd %s /S /Q" % (results_dir))
if not os.path.exists(results_dir):
    os.makedirs(results_dir)
    print("makedir " + results_dir)
    
for e in executables:
    file_paths = e.split("\\")
    file_name = file_paths[-1]
    import_file = results_dir+ file_name + ".txt"
    #use dumpbin.exe to export the kernel api called by each dll or exe
    os.system("%s /IMPORTS %s > %s" % ('"E:\\Program Files (x86)\\Microsoft Visual Studio 14.0\\VC\\bin\\x86_amd64\\dumpbin.exe"', e,import_file));
    if not os.path.exists(import_file):
        print("不存在："+ import_file)
        continue
    file = codecs.open(import_file, encoding="utf-8")
    find = False
    begin_find = False
    while(True):
        line = file.readline()
        if line == "":
            file.close()
            break
        if begin_find:
            if line.find("InitializeCriticalSectionEx") != -1:
                file.close()
                find = True
                print(e + ": " + line)
                break
        #Just find the target API under KERNEL32.dll
        if line.find("KERNEL32.dll") != -1:
            begin_find = True
            continue
        if begin_find == True and line.find(".dll") != -1:
            file.close()
            break
        
