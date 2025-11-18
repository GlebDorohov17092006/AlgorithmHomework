#include "start_positional.h"
#include "node.h"
#include "positional_equal.h"
#include "positional_hash.h"
#include <iostream>
#include <queue>
#include <unordered_map>
#include <functional>
#include <cmath>
#include <memory>
#include <algorithm>

StartPositional::StartPositional(Positional *start_positional)
{
    this->start_positional = start_positional;
    search_min_path();
}

int StartPositional::number_of_inversions() const
{
    std::vector<int> matrix_array;
    int result = 0;
    for (int i{0}; i < 4; ++i)
    {
        for (int j{0}; j < 4; ++j)
        {
            int value = start_positional->get_matrix()[i][j];
            if (value != 0)
            {
                matrix_array.push_back(value);
            }
        }
    }

    for (size_t i{0}; i < matrix_array.size(); ++i)
    {
        for (size_t j{i + 1}; j < matrix_array.size(); ++j)
        {
            if (matrix_array[i] > matrix_array[j])
            {
                ++result;
            }
        }
    }

    return result;
}

bool StartPositional::has_path() const
{
    int inversions = number_of_inversions();
    int empty_row = start_positional->get_empty_cage().first;

    return (inversions + empty_row) % 2 == 1;
}

void StartPositional::search_min_path()
{
    if (!this->has_path())
    {
        min_path = -1;
        return;
    }

    if (start_positional->get_correct_positional())
    {
        min_path = std::vector<Positional *>{start_positional};
        return;
    }

    std::priority_queue<Node, std::vector<Node>, std::greater<Node>> open_set;
    std::unordered_map<Positional *, Positional *, PositionalHash, PositionalEqual> came_from;
    std::unordered_map<Positional *, int, PositionalHash, PositionalEqual> g_score;

    Node start_node;
    start_node.positional = start_positional;
    start_node.g_cost = 0;
    start_node.h_cost = start_positional->manhattan_distance();

    open_set.push(start_node);
    g_score[start_positional] = 0;

    while (!open_set.empty())
    {
        Node current = open_set.top();
        open_set.pop();

        Positional *current_pos = current.positional;

        if (current_pos->get_correct_positional())
        {
            std::vector<Positional *> path;
            Positional *node = current_pos;
            while (node != nullptr)
            {
                path.push_back(node);
                auto it = came_from.find(node);
                if (it != came_from.end())
                {
                    node = it->second;
                }
                else
                {
                    node = nullptr;
                }
            }
            std::reverse(path.begin(), path.end());
            min_path = path;
            return;
        }

        auto neighbors = current_pos->get_neighbors();
        for (auto &neighbor_ptr : neighbors)
        {
            Positional *neighbor = neighbor_ptr.get();
            int tentative_g_score = g_score[current_pos] + 1;

            if (g_score.find(neighbor) == g_score.end() || tentative_g_score < g_score[neighbor])
            {
                came_from[neighbor] = current_pos;
                g_score[neighbor] = tentative_g_score;

                Node neighbor_node;
                neighbor_node.positional = neighbor;
                neighbor_node.g_cost = tentative_g_score;
                neighbor_node.h_cost = neighbor->manhattan_distance();

                open_set.push(neighbor_node);
                neighbor_ptr.release();
            }
        }
    }
}

void StartPositional::print_min_path(std::ostream &os) const
{
    try
    {
        auto &path = std::get<std::vector<Positional *>>(min_path);
        for (size_t i{0}; i < path.size(); ++i)
        {
            os << "State " << i << ":" << '\n';
            path[i]->print_matrix(os);
            if (i < path.size() - 1)
            {
                os << "v" << '\n';
            }
        }
    }
    catch (const std::bad_variant_access &e)
    {
        os << "No solution exists!";
    }
}

std::variant<std::vector<Positional *>, int> StartPositional::get_min_path() const
{
    return min_path;
}