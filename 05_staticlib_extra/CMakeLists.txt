# CMake 最低版本要求
cmake_minimum_required (VERSION 2.8)

# 项目信息
project (cmake-practice)

#设置debug版本后缀
SET( CMAKE_DEBUG_POSTFIX "d" CACHE STRING "add a postfix, usually d on windows" )

#添加子目录
add_subdirectory(example)