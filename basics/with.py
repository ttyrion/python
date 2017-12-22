
#参考：https://www.ibm.com/developerworks/cn/opensource/os-cn-pythonwith/
#with和上下文管理器（实现了上线问管理协议）合作，可以实现自动关闭文件、自动获取和释放线程锁等。

with open("sample.txt", "r") as file:
    for line in file:
        print(line)