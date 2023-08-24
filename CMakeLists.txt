cmake_minimum_required(VERSION 3.27)
project(aa)
enable_language(C)
enable_language(CXX)
if(APPLE)
    enable_language(OBJC)
    enable_language(OBJCXX)
endif()
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_POSITION_INDEPENDENT_CODE TRUE)

set_property(GLOBAL PROPERTY USE_FOLDERS ON)
# list(APPEND CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/../common/cmake")
# include(Platform)
# include(RuntimeSpec)

list(PREPEND CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/build)
list(PREPEND CMAKE_PREFIX_PATH ${CMAKE_SOURCE_DIR}/build)
message(${CMAKE_PREFIX_PATH})

# find_package(BZip2 REQUIRED NO_MODULE)
find_package(BZip2 REQUIRED)
find_package(GTest REQUIRED)
# ...
message("${GTest_FOUND}")
message("${GTEST_MAIN_LIBRARIES}")
message("${GTEST_ROOT}")
message("${GTEST_BOTH_LIBRARIES}")
message("${GTest_LIBRARIES}")
message("${GTEST_INCLUDE_DIRS}")
message("${GTEST_LIBRARIES}")
message("${BZip2_LIBRARIES}")
message("${BZIP2_INCLUDE_DIRS}")
add_executable(aaa a.cpp)
target_link_libraries(
    aaa
    BZip2::BZip2
    GTest::gtest
    GTest::gtest_main
)
# add_custom_target(genexdebug COMMAND ${CMAKE_COMMAND} -E echo "$<TARGET_PROPERTY:gtest::gtest,INTERFACE_LINK_LIBRARIES>")
file(GENERATE
     OUTPUT ${CMAKE_SOURCE_DIR}/log.txt
     CONTENT "$<TARGET_PROPERTY:gtest::gtest,INCLUDE_DIRECTORIES>"
)
