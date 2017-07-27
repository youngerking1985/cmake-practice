#设置编译所需要的包含目录
INCLUDE_DIRECTORIES(${PROJECT_SOURCE_DIR}/math/include)
#设置编译所需要的包含库目录
LINK_DIRECTORIES(${PROJECT_SOURCE_DIR}/math/lib)

#设置需要编译的文件
SET(APP_SRC main.cpp)


#设置执行程序
ADD_EXECUTABLE(example ${APP_SRC})
SET_TARGET_PROPERTIES( example PROPERTIES DEBUG_POSTFIX "${CMAKE_DEBUG_POSTFIX}" )

#设置链接库
TARGET_LINK_LIBRARIES(example debug mathd)
TARGET_LINK_LIBRARIES(example optimized math)

#自定义安装目录
INSTALL (TARGETS example DESTINATION bin)

#消息输出测试
MESSAGE ("example---------------------------------")
MESSAGE ("bin_dir " + ${PROJECT_BINARY_DIR})
MESSAGE ("source_dir " + ${PROJECT_SOURCE_DIR})
MESSAGE ("get env " + $ENV{OSGDIR}"")
