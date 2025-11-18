#pragma once

#include "positional.h"

struct Node
{
    Positional *positional;
    int g_cost;
    int h_cost;
    int f_cost() const;
    bool operator>(const Node &other) const;
};