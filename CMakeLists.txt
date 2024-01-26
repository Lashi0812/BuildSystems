cmake_minimum_required(VERSION 3.27)
project(MyApp LANGUAGES C CXX)

add_subdirectory(CMAKE/01_Minimal)
add_subdirectory(CMAKE/02_Build_Simple_Target/lib_static)
add_subdirectory(CMAKE/02_Build_Simple_Target/lib_dynamic)
add_subdirectory(CMAKE/02_Build_Simple_Target/src)