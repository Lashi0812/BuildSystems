#include <iostream>

extern "C" void dynamic_function();

int main() {
    std::cout << "Calling dynamic_function from main..." << std::endl;
    dynamic_function();
    return 0;
}
