#pragma once

#include <vector>
#include <memory>
#include <ostream>

class Positional
{
public:
    Positional(std::vector<std::vector<int>> matrix);
    std::vector<std::unique_ptr<Positional>> get_neighbors() const;
    std::vector<std::vector<int>> get_matrix() const;
    std::pair<int, int> get_empty_cage() const;
    bool get_correct_positional() const;
    void print_matrix(std::ostream &os) const;
    int manhattan_distance() const;

private:
    std::vector<std::vector<int>> matrix;
    std::pair<int, int> empty_cage;
    bool correct_positional;
    void validation_matrix();
    bool has_correct_positional() const;
};
