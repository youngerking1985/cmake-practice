# -*- coding: cp936 -*-

import os
import sys
import string
import subprocess


#命令行参数
# ALL_TARGET = "vc"
# ALL_TARGET = "mingw"
# ALL_TARGET = "ndk"
# ALL_TARGET = "nc"


#外部工具和路径设置 
CMAKE_EXE = r'"d:/Program Files/CMake/bin/cmake.exe"'
CMAKE_VC_PLATFORM = r'"Visual Studio 12 2013 Win64"' #根据cmake的产生设置 比如 Visual Studio 11 2012 Win64
BUILD_DYNAMIC_LINK_LIBRARY = False
BOOST_ARCH = 'x86' #可选配置 x86 没有x64只能设置BOOST_ADDRESS_MODEL为64
BOOST_ADDRESS_MODEL = '64'  #可选配置 32 64
FFMPEG_ADDRESS_MODEL = '64' #可选配置 32 64
PTHREADS_BUILD_PROFILE = '-DPTHREADS_BUILD_CPP' #可选配置 PTHREADS_BUILD_CPP PTHREADS_BUILD_SEH


#
#辅助函数
#

def my_make_build_dir(str_project_name):
    print "mkdir build path"    
    os.system( "mkdir build_vc_" + str_project_name)
    os.chdir("build_vc_" + str_project_name)    


#获取当前文件目录
def cur_file_dir():
     path = sys.path[0]
     if os.path.isdir(path):
         return path
     elif os.path.isfile(path):
         return os.path.dirname(path)

#运行命令
def my_exec( str_target, cmake_str ):
    print "exec - "  + cmake_str
    
    # if(str_target == "vc"):
    ps = subprocess.Popen(cmake_str);
    ps.wait();
    # else:
        # os.system(cmake_str)
    
#cmake 配置设置 
def my_configure( str_target , str_config , str_project_name, is_osg = False , over_debug_postfix = True ,is_opencv = False):
    # is_osg 只是用来在ndk编译时提高一个目录级别
    cmake_string = CMAKE_EXE
    
    if over_debug_postfix :
        cmake_string += r' -DCMAKE_DEBUG_POSTFIX="d"'
    
    if str_target == "vc" :
        cmake_string += ' -G ' + CMAKE_VC_PLATFORM
        cmake_string += ' -DCMAKE_INSTALL_PREFIX="./shared_vc/" '       
    
    # cmake_string += "  -DCMAKE_BUILD_TYPE=Debug/Release"
    cmake_string += ' ' + str_config+ ' ../' + str_project_name

    #获取CMakeLists.txt路径
    # print "curpath " + cur_file_dir()
    # cmakefile = cur_file_dir() + "/CMakeLists.txt" 
    # cmake_string += ' ' + cmakefile    
    # os.chdir( "../build_vc")

    my_make_build_dir(str_project_name)
    my_exec( str_target, cmake_string )

#vc编译
def my_build( str_target , only_release = False):
    if(str_target == "vc" or str_target == "cw" ):
        if( not only_release ):
            os.system('msbuild install.vcxproj /p:Configuration=Debug')
            pass
        os.system('msbuild install.vcxproj /p:Configuration=Release')
# main
def main():

    ALL_TARGET = "vc" #默认vc
    PROJECT_NAME = ""
    if len(sys.argv) >= 2:
        ALL_TARGET = sys.argv[1]
        PROJECT_NAME = sys.argv[2]
    else:
        print "need vc and project_name as args"
        return
    
    print( ALL_TARGET +" >> "+ PROJECT_NAME )

    my_configure(ALL_TARGET, "", PROJECT_NAME)
    my_build(ALL_TARGET)

main()