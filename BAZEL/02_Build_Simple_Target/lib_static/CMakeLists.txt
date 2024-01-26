add_library(staticlib STATIC
            add.cpp
            mul.cpp            
)       
target_include_directories(staticlib PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})