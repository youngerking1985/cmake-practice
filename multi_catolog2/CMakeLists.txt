# CMake 最低版本要求
cmake_minimum_required (VERSION 2.8)

# 项目信息
project (cmake-practice)

#加入一个配置文件，用于处理CMkae对源码的处理
configure_file(
	"${PROJECT_SOURCE_DIR}/config.h.in"
	"${PROJECT_SOURCE_DIR}/config.h"
)

#是否使用自己的MathFunctions库
option(USE_MYMATH "Use provided math implementation" ON)

if (USE_MYMATH)
	include_directories ("${PROJECT_SOURCE_DIR}/math")
	add_subdirectory (math)
	set (EXTRA_LIBS ${EXTRA_LIBS} MathFunctions)
endif(USE_MYMATH)

#查找当前目录下的所有源文件；并将名称保存到 DIR_SRCS变量中
aux_source_directory(. DIR_SRCS)

#自定生成指定目标
add_executable(multi_catalog DIR_SRCS)

#添加链接库
target_link_libraries(multi_catalog ${EXTRA_LIBS})
