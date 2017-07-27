# CMake 最低版本要求
cmake_minimum_required (VERSION 2.8)

#设置库编译需要的文件
set(LIB_SRC MathFunctions.cpp)

#自定生成指定目标
add_library(math ${LIB_SRC})

#设置文件输出路径
set(LIBRARY_OUTPUT_PATH ${PROJECT_BINARY_DIR}/lib)


#自定义安装目录
install(TARGETS math DESTINATION lib)
install (FILES "${PROJECT_SOURCE_DIR}/math/MathFunctions.h" DESTINATION include)

#消息输出测试
message ("math---------------------------------")
message ("bin_dir " + ${PROJECT_BINARY_DIR})
message ("source_dir " + ${PROJECT_SOURCE_DIR})
message ("get env " + $ENV{OSGDIR}"")
