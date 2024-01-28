cmake_minimum_required(VERSION 3.27)
project(standard_flag)

add_library(animallib
    SHARED
    src/Animal.cpp
    src/Cat.cpp
    src/Dog.cpp
)

target_include_directories(animallib PUBLIC include)
set_target_properties(animallib 
    PROPERTIES
    CXX_STANDARD 14
    CXX_STANDARD_REQUIRED OFF
    CXX_EXTENSIONS ON
    POSITION_INDEPENDENT_CODE 1
)

add_executable(07_main_sf src/animal-farm.cpp)
set_target_properties(07_main_sf
    PROPERTIES
    CXX_STANDARD 14
    CXX_STANDARD_REQUIRED OFF
    CXX_EXTENSIONS ON
)
target_link_libraries(07_main_sf PRIVATE animallib)

