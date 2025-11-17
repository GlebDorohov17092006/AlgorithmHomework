#pragma once
#include "positional.h"
#include <variant>
#include <sstream>

class StartPositional
{
public:
    StartPositional(Positional *start_positional);
    std::variant<std::vector<Positional *>, int> get_min_path() const;
    void print_min_path(std::ostream &os) const;

private:
    Positional *start_positional;
    std::variant<std::vector<Positional *>, int> min_path;
    bool has_path() const;
    int number_of_inversions() const;
    void search_min_path();
};