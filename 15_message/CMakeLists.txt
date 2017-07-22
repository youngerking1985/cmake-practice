# CMake 最低版本要求
cmake_minimum_required (VERSION 2.8)

#消息输出测试
message ("Hello World")
message ("bin_dir " + ${PROJECT_BINARY_DIR})
message ("source_dir " + ${PROJECT_SOURCE_DIR})
message ("get env " + $ENV{OSGDIR}"")
