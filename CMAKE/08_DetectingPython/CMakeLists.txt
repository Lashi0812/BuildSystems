cmake_minimum_required(VERSION 3.27)
project(detecting_python LANGUAGES NONE)
find_package(Python3 REQUIRED)
execute_process(
    COMMAND
        ${Python3_EXECUTABLE} "-c" "print('Hello')"   
    RESULT_VARIABLE _status
    OUTPUT_VARIABLE _output
    ERROR_QUIET
    OUTPUT_STRIP_TRAILING_WHITESPACE
)

message(STATUS "RESULT_VARIABLE is : ${_status}")
message(STATUS "OUTPUT_VARIABLE is : ${_output}")
include(CMakePrintHelpers)
cmake_print_variables(_status _output)


