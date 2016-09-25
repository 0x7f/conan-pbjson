project(pbjson)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

include_directories(${CMAKE_SOURCE_DIR}/src)

add_library(${PROJECT_NAME} src/bin2ascii.h src/pbjson.cpp src/pbjson.hpp)
target_link_libraries(${PROJECT_NAME} ${CONAN_LIBS})
