add_library(dynamiclib SHARED dynamic.cpp)
target_link_libraries(dynamiclib PRIVATE staticlib)