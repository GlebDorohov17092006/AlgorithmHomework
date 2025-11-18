#pragma once

#include "positional.h"

struct PositionalHash
{
    size_t operator()(Positional *pos) const;
};