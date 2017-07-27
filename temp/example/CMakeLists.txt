#设置编译所需要的包含目录
include_directories(${PROJECT_SOURCE_DIR}/math)

#设置需要编译的文件
set(APP_SRC main.cpp)

#设置文件输出路径
set(EXECUTABLE_OUTPUT_PATH ${PROJECT_BINARY_DIR}/bin)

#设置执行程序
add_executable(example ${APP_SRC})

#设置链接库
target_link_libraries(example math)

#自定义安装目录
install (TARGETS example DESTINATION bin)

#消息输出测试
message ("example---------------------------------")
message ("bin_dir " + ${PROJECT_BINARY_DIR})
message ("source_dir " + ${PROJECT_SOURCE_DIR})
message ("get env " + $ENV{OSGDIR}"")
