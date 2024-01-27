cmake_minimum_required(VERSION 3.27)
project(controlling_complier_flag LANGUAGES CXX)

message(STATUS "C++ Compiler Flags ${CMAKE_CXX_FLAGS}")

list(APPEND flags "-fPIC" "-Wall")
if(NOT WIN32)
    list(APPEND flags "-Wextra" "-Wpedantic")
endif()

add_library(geometry
    STATIC
    src/circle.cpp
    src/square.cpp
)

target_include_directories(geometry PUBLIC includes)
target_compile_options(geometry PRIVATE ${flags})

add_executable(main src/main.cpp)
target_compile_options(main PRIVATE "-fPIC")
target_link_libraries(main geometry)
