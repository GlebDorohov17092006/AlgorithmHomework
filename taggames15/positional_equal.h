#pragma once
#include "positional.h"

struct PositionalEqual
{
    bool operator()(Positional *a, Positional *b) const;
};