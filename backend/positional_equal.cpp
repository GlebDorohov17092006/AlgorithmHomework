#include "positional_equal.h"

bool PositionalEqual::operator()(Positional *a, Positional *b) const
{
    auto matrix_a = a->get_matrix();
    auto matrix_b = b->get_matrix();
    for (int i = 0; i < 4; ++i)
    {
        for (int j = 0; j < 4; ++j)
        {
            if (matrix_a[i][j] != matrix_b[i][j])
            {
                return false;
            }
        }
    }
    return true;
}