#include "operations.hpp"
#include <iostream>

int main(int argc, char *argv[]) {
    std::cout << "ADD 5 + 4 = " << add(5, 4) << std::endl;
    std::cout << "MUL 5 * 4 = " << mul(5, 4) << std::endl;
    return EXIT_SUCCESS;
}
