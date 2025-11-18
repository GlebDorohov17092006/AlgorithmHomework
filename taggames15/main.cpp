#include "start_positional.h"
#include "positional.h"
#include <iostream>

int main()
{
    std::cout << "=== 15-PUZZLE SOLVER ===" << std::endl;

    std::vector<std::vector<int>> matrix = {
        {1, 2, 3, 4},
        {5, 0, 6, 7},
        {9, 10, 11, 8},
        {13, 14, 15, 12}};

    std::cout << "Initial position:" << std::endl;
    Positional pos(matrix);
    pos.print_matrix(std::cout);

    std::cout << "\nSolving..." << std::endl;
    StartPositional solver(&pos);

    auto path = solver.get_min_path();

    if (std::holds_alternative<int>(path))
    {
        std::cout << "NO SOLUTION FOUND!" << std::endl;
    }
    else
    {
        auto &path_vec = std::get<std::vector<Positional *>>(path);
        std::cout << "SOLUTION FOUND! Steps: " << path_vec.size() - 1 << std::endl;
        std::cout << "\nSolution path:" << std::endl;
        solver.print_min_path(std::cout);
    }

    return 0;
}