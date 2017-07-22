# -*- coding: cp936 -*-

import os
import sys
import string
import subprocess


#�����в���
# ALL_TARGET = "vc"
# ALL_TARGET = "mingw"
# ALL_TARGET = "ndk"
# ALL_TARGET = "nc"


#�ⲿ���ߺ�·������
CMAKE_EXE = r'"d:/Program Files/CMake/bin/cmake.exe"'
CMAKE_VC_PLATFORM = r'"Visual Studio 12 2013 Win64"' #����cmake�Ĳ������� ���� Visual Studio 11 2012 Win64
BUILD_DYNAMIC_LINK_LIBRARY = False
BOOST_ARCH = 'x86' #��ѡ���� x86 û��x64ֻ������BOOST_ADDRESS_MODELΪ64
BOOST_ADDRESS_MODEL = '64'  #��ѡ���� 32 64
FFMPEG_ADDRESS_MODEL = '64' #��ѡ���� 32 64
PTHREADS_BUILD_PROFILE = '-DPTHREADS_BUILD_CPP' #��ѡ���� PTHREADS_BUILD_CPP PTHREADS_BUILD_SEH


#
#��������
#

def my_exec( str_target, cmake_str ):
    print "exec - "  + cmake_str
    
    # if(str_target == "vc"):
    ps = subprocess.Popen(cmake_str);
    ps.wait();
    # else:
        # os.system(cmake_str)
    

def my_configure( str_target , str_config ,is_osg = False , over_debug_postfix = True ,is_opencv = False):
    # is_osg ֻ��������ndk����ʱ���һ��Ŀ¼����
    cmake_string = CMAKE_EXE
    
    if over_debug_postfix :
        cmake_string += r' -DCMAKE_DEBUG_POSTFIX="d"'
    
    if str_target == "vc" :
        cmake_string += ' -G ' + CMAKE_VC_PLATFORM
        cmake_string += ' -DCMAKE_INSTALL_PREFIX="./shared_vc/" '
        
    cmake_string += ' ' + str_config+ ''
    
    my_exec( str_target, cmake_string )

def my_build( str_target , only_release = False):
    if(str_target == "vc" or str_target == "cw" ):
        if( not only_release ):
            os.system('msbuild MathFunctions.vcxproj /p:Configuration=Debug')
            os.system('msbuild multi_catalog.vcxproj /p:Configuration=Debug')
            pass
        os.system('msbuild MathFunctions.vcxproj /p:Configuration=Release')    
        os.system('msbuild multi_catalog.vcxproj /p:Configuration=Release')

    os.chdir( "../../..")
    
my_configure("vc", "")
my_build("vc")