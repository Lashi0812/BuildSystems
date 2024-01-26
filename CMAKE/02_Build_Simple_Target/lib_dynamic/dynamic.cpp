#include "operations.h"
#include <iostream>

extern "C" void dynamic_function()
{
    int result_add = add(10, 5);
    int result_mul = mul(3, 4);

    std::cout << "Dynamic Function - Addition: 10 + 5 = " << result_add << std::endl;
    std::cout << "Dynamic Function - Multiplication: 3 * 4 = " << result_mul << std::endl;
}
