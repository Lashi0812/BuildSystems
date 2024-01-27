cmake_minimum_required(VERSION 3.27)
project(build_type LANGUAGES CXX CUDA)

if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release CACHE STRING "Build Type" FORCE)
endif()

message(STATUS "Build Type : ${CMAKE_BUILD_TYPE}")

message(STATUS "CXX Flags , Debug configuration : ${CMAKE_CXX_FLAGS_DEBUG}")
message(STATUS "CXX Flags , Release configuration : ${CMAKE_CXX_FLAGS_RELEASE}")
message(STATUS "CXX Flags , Release configuration with debug info : ${CMAKE_CXX_FLAGS_RELWITHDEBINFO}")
message(STATUS "CXX flags , minimal Release configuration: ${CMAKE_CXX_FLAGS_MINSIZEREL}")

message(STATUS "CUDA Flags , Debug configuration : ${CMAKE_CUDA_FLAGS_DEBUG}")
message(STATUS "CUDA Flags , Release configuration : ${CMAKE_CUDA_FLAGS_RELEASE}")
message(STATUS "CUDA Flags , Release configuration with debug info : ${CMAKE_CUDA_FLAGS_RELWITHDEBINFO}")
message(STATUS "CUDA flags , minimal Release configuration: ${CMAKE_CUDA_FLAGS_MINSIZEREL}")