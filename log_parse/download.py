import urllib
import urllib.request
from html.parser import HTMLParser
import os

class MyHtmlParser(HTMLParser):
    files = []
    def __init__(self):
        HTMLParser.__init__(self)
        
    def handle_starttag(self, tag, attributes):
        if tag == "a":
            #print(attributes)
            for name,value in attributes:
                if name == 'href':
                    #value here represends the file_name which locates relatively
                    self.files.append(value)
                    
    def get_files(self):
        return self.files
'''
下载url( of a ftp directory)里面的所有lib, dll, pdb文件
'''
def download_cupid_files(url, local_directory, down):
    html_page=urllib.request.urlopen(url)
    data = html_page.read()
    parser = MyHtmlParser()
    parser.feed(str(data, encoding="utf-8"))
    file_list = parser.get_files()
    print(file_list);
    
    if url[-1] != "/":
        url += "/"
    if local_directory[-1] != "\\":
        local_directory += "\\"
    print("downloading files in:" + url)
    
    log_file = []
    for file in file_list:
        if file.upper().endswith(".LOG"):
            log_file.append(file)
    
    if down == False:
        return log_file;
    
    for file in log_file:
        full_url = url + file
        file_request = urllib.request.urlopen(full_url)
        file_data = file_request.read()
        tmp_file = open(local_directory + file, "wb")
        tmp_file.write(file_data)
        print("downloading " + file + " success.")
    return log_file
            
            
            