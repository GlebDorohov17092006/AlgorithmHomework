#include "positional.h"
#include <stdexcept>
#include <algorithm>

Positional::Positional(std::vector<std::vector<int>> matrix)
{
    this->matrix = matrix;
    validation_matrix();
    correct_positional = has_correct_positional();
}

void Positional::validation_matrix()
{
    if (matrix.size() != 4)
    {
        throw std::out_of_range("The size of the matrix does not match the required size");
    }

    for (const auto &row : matrix)
    {
        if (row.size() != 4)
        {
            throw std::out_of_range("The size of the matrix does not match the required size");
        }
    }

    std::vector<int> value_matrix(16, 0);
    for (int i{0}; i < 4; ++i)
    {
        for (int j{0}; j < 4; ++j)
        {
            int value = matrix[i][j];
            if (value < 0 || value >= 16)
            {
                throw std::out_of_range("The values of the matrix go beyond the corresponding boundaries");
            }

            if (value_matrix[value] > 0)
            {
                throw std::out_of_range("The value occurs twice in the matrix");
            }

            value_matrix[value] += 1;

            if (value == 0)
            {
                empty_cage = {i, j};
            }
        }
    }
}

bool Positional::has_correct_positional() const
{
    std::vector<std::vector<int>> target = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12},
        {13, 14, 15, 0}};

    return matrix == target;
}

std::vector<std::vector<int>> Positional::get_matrix() const
{
    return matrix;
}

std::vector<std::unique_ptr<Positional>> Positional::get_neighbors() const
{
    int motions[4][2]{{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
    std::vector<std::unique_ptr<Positional>> result;
    for (auto &motion : motions)
    {
        int new_i = empty_cage.first + motion[0];
        int new_j = empty_cage.second + motion[1];

        if (new_i >= 0 && new_i < 4 && new_j >= 0 && new_j < 4)
        {
            std::vector<std::vector<int>> neighbour_matrix = matrix;
            std::swap(neighbour_matrix[empty_cage.first][empty_cage.second],
                      neighbour_matrix[new_i][new_j]);

            result.push_back(std::make_unique<Positional>(neighbour_matrix));
        }
    }
    return result;
}

bool Positional::get_correct_positional() const
{
    return correct_positional;
}

void Positional::print_matrix(std::ostream &os) const
{
    for (int i{0}; i < 4; ++i)
    {
        for (int j{0}; j < 4; ++j)
        {
            os << matrix[i][j] << " ";
        }
        os << '\n';
    }
}

int Positional::manhattan_distance() const
{
    int distance = 0;
    for (int i = 0; i < 4; ++i)
    {
        for (int j = 0; j < 4; ++j)
        {
            int value = matrix[i][j];
            if (value != 0)
            {
                int target_i = (value - 1) / 4;
                int target_j = (value - 1) % 4;
                distance += std::abs(i - target_i) + std::abs(j - target_j);
            }
        }
    }
    return distance;
}

std::pair<int, int> Positional::get_empty_cage() const
{
    return empty_cage;
}