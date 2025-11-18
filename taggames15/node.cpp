#include "node.h"

int Node::f_cost() const
{
    return g_cost + h_cost;
}

bool Node::operator>(const Node &other) const
{
    return f_cost() > other.f_cost();
}
