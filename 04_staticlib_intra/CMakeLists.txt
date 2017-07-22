# CMake 最低版本要求
cmake_minimum_required (VERSION 2.8)

# 项目信息
project (cmake-practice)


set(LIB_SRC math/MathFunctions.cpp)
set(APP_SRC example/main.cpp)

#自定生成指定目标
add_library(tempLib ${LIB_SRC})
add_executable(temp ${APP_SRC})

#库链接设置
target_link_libraries(temp tempLib)

#自定义安装目录
install (TARGETS temp DESTINATION bin)
install(TARGETS tempLib DESTINATION lib)
install (FILES "${PROJECT_SOURCE_DIR}/math/MathFunctions.h" DESTINATION include)

#消息输出测试
message ("---------------------------------")
message ("Hello World")
message ("bin_dir " + ${PROJECT_BINARY_DIR})
message ("source_dir " + ${PROJECT_SOURCE_DIR})
message ("get env " + $ENV{OSGDIR}"")
