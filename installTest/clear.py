# import shutil
# import os
# # shutil.rmtree(r'd:/test')
# print "test"

# def findBuild()

# for i in os.listdir('.'):
#     if os.path.isdir(i):
#         print i
#         print os.path.


import os, sys
import os.path
import shutil
 
def cur_file_dir():
     path = sys.path[0]
     if os.path.isdir(path):
         return path
     elif os.path.isfile(path):
         return os.path.dirname(path)
# rootdir = r"d:/temp"
rootdir = cur_file_dir()
print "current path is " + rootdir

for parent,dirnames,filenames in os.walk(rootdir):
    for dirname in dirnames:
        theList = ["Debug", "Release", "x64", "CMakeFiles", "shared_vc"]
        if dirname in theList:
            shutil.rmtree(parent+"/"+dirname)
            print "remove dir: " + (parent+"/"+dirname)
        if ".dir" in dirname:
            shutil.rmtree(parent+"/"+dirname)
            print "remove dir: " + (parent+"/"+dirname)

    for filename in filenames:
        theList = [".vcxproj", ".filters", ".cmake", ".sln", ".suo", ".sdf"]
        theList2 = ["CMakeCache.txt"]
        filenameext = os.path.splitext(filename)[1]
        if(filename in theList2):
            os.remove(parent + "/" + filename)
            print "remove file: " + (parent + "/" + filename)
            continue

        if(filenameext in theList):
            os.remove(parent + "/" + filename)
            print "remove file: " + (parent + "/" + filename)

os.system("pause")