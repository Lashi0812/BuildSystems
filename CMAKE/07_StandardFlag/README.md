# Setting the standard for the language

* `CXX_STANDARD` mandates the standard that we would like to have.
* `CXX_EXTENSIONS` tells CMake to only use compiler flags that will enable the ISO C++ standard, without compiler-specific extensions.
```shell
gcc .. -std=c++14   .. # CXX_EXTENSIONS OFF
gcc .. -std=gnu++14 .. # CXX_EXTENSIONS ON
```
* `CXX_STANDARD_REQUIRED` specifies that the version of the standard chosen is required. If this version is not available, CMake will stop configuration with an error. When this property is set to OFF, CMake will look for next latest version of the standard, until a proper flag has been set. This means to first look for C++14, then C++11, then C++98.