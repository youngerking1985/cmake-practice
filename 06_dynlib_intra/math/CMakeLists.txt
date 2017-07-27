# CMake 最低版本要求
cmake_minimum_required (VERSION 2.8)

#设置库编译需要的文件
set(LIB_SRC MathFunctions.cpp)

#定义宏
add_definitions("-DMATH_BUILD")

#自定生成指定目标
add_library(math SHARED ${LIB_SRC})

#设置文件输出路径
set(LIBRARY_OUTPUT_PATH ${PROJECT_BINARY_DIR}/lib)
# set(EXECUTABLE_OUTPUT_PATH, ${PROJECT_BINARY_DIR}/bin)


#自定义安装目录
install(TARGETS math DESTINATION lib)
install (FILES "${PROJECT_SOURCE_DIR}/math/MathFunctions.h" DESTINATION include)

#消息输出测试
message ("mat some path---------------------------------")
message ("bin_dir " + ${PROJECT_BINARY_DIR})
message ("source_dir " + ${PROJECT_SOURCE_DIR})
message ("get env " + $ENV{OSGDIR}"")
message ("CMAKE_INCLUDE_PATH" } ${CMAKE_INCLUDE_PATH})
message ("CMAKE_CURRENT_SOURCE_DIR" } ${CMAKE_CURRENT_SOURCE_DIR})
message ("CMAKE_CURRENT_BINARY_DIR" } ${CMAKE_CURRENT_BINARY_DIR})

