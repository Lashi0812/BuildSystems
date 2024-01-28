# Detecting the Python

use py_binary for execution the python file 
```sh
py_binary(
    name = "hello",
    srcs = ["hello.py"],
    main = "hello.py",
)
```