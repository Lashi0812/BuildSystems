import sys
print(sys.path)
from Python_build.greet import greet

if __name__ == "__main__":
    print(f"Hello {greet()}")