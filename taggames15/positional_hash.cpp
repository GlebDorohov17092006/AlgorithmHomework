#include "positional_hash.h"

size_t PositionalHash::operator()(Positional *pos) const
{
    size_t hash = 0;
    auto matrix = pos->get_matrix();
    for (const auto &row : matrix)
    {
        for (int val : row)
        {
            hash = hash * 31 + val;
        }
    }
    return hash;
}