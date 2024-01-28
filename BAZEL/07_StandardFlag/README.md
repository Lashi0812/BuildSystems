# Setting the standard for the language

## Per-target

We can apply the flag directly to the each target directly using the copts

```bazel
copts = ["-std=c++14"],
```

## Project level

To apply for all the target we can use buildrc file or command line .

### command line

we can apply `--cxxopt="-std=c++14"` for target we build

```shell
bazel build --subcommands=pretty_print --cxxopt="-std=c++14" //BAZEL/07_StandardFlag:07_main 
```

### buildrc

```shell
build --cxxopt="-std=c++14"
```
