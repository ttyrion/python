class TFile(object):
    #An object is created by __new__, but not __init__
    def __new__(cls, *args, **kargs):
        print("__new__ called.")
        return super(TFile,cls).__new__(cls,*args, **kargs)
    
    #__new__ would call __init__ after creating an object
    def __init__(self, obj_name):
        self.name = obj_name
        print("%s init." % self.name)
        
    def __del__(self):
        print("%s delete." % self.name)
    
    def open(self, path, flag):
        self.file_ = open(path,flag)
        
    def read(self):
        return self.file_.read()
        
    def close(self):
        return self.file_.close()
        
    file_ = None
    name_ = ""

#A was the first being deleted, because its reference count was 0 After(mind this word) C being created. 
a = TFile("A")
b = TFile("B")
a = TFile("C")

# a.open("sample.txt", "r")
# content = a.read()
# print(content)
# a.close()

"""输出如下：
__new__ called.
A init.
__new__ called.
B init.
__new__ called.
C init.
A delete.
C delete.
B delete.
"""
