# CMake 最低版本要求
cmake_minimum_required (VERSION 2.8)

# 项目信息
project (cmake-practice)

#查找当前目录下的所有源文件；并将名称保存到 DIR_SRCS变量中
aux_source_directory(. DIR_SRCS)

#添加math子目录
add_subdirectory(math)

#自定生成指定目标
add_executable(multi_catalog main.cpp)

#添加链接库
target_link_libraries(multi_catalog MathFunctions)
